# Surplus Food v3 — Change Log & Migration Guide

## What changed (and why)

---

### 1. JWT Authentication + bcrypt password hashing

**Files changed:**
- `backend/app/core/security.py` ← NEW
- `backend/app/routes/auth_routes.py`
- `backend/app/services/hotel_service.py`
- `backend/app/services/ngo_service.py`
- `backend/app/services/volunteer_service.py`
- `backend/app/schemas/auth_schemas.py`
- `backend/app/schemas/all_schemas.py` (added `password` to all Create schemas)
- `backend/app/models/base_models.py` (added `password` field to all user models)
- `frontend/src/pages/Login.jsx` (added password field)
- `frontend/src/pages/Register.jsx` (added password + confirm password fields)
- `frontend/src/services/api.js` (JWT interceptor on every request)
- `frontend/src/context/AuthContext.jsx` (stores + forwards `access_token`)

**What it does:**
- Registration: password is hashed with **bcrypt** before storing in MongoDB. The hash is never returned to the client.
- Login (`POST /auth/login`): verifies password via `passlib`, returns a signed **JWT** (`access_token` in response body). Legacy accounts without a stored password use a plain-text fallback until migrated.
- Frontend: `api.js` has an Axios request interceptor that reads `access_token` from `localStorage` and attaches `Authorization: Bearer <token>` to every API call automatically.
- JWT secret is read from env var `SECRET_KEY`. Token expiry defaults to 24 h (configurable via `ACCESS_TOKEN_EXPIRE_MINUTES`).

**Migration note for existing users:**
Existing MongoDB documents have no `password` field. The auth route handles this gracefully: if the stored `password` doesn't start with `$2` (bcrypt prefix), it falls back to plain-text comparison. Set plain-text passwords in the DB for existing accounts, then prompt users to reset next time they log in.

---

### 2. MongoDB `$lookup` aggregation (bye-bye N+1 queries)

**File changed:** `backend/app/services/food_service.py`

**Before (v2):**
```python
# Called once per food document — O(N) round trips
for f in foods:
    hotel = await db["hotels"].find_one({"_id": ObjectId(f["hotel_id"])})
```

**After (v3):**
```python
# Single aggregation pipeline — O(1) round trips
pipeline = [
    {"$match": {"status": "available"}},
    {"$addFields": {"hotel_oid": {"$toObjectId": "$hotel_id"}}},
    {"$lookup": {"from": "hotels", "localField": "hotel_oid",
                 "foreignField": "_id", "as": "_hotel"}},
    {"$unwind": {"path": "$_hotel", "preserveNullAndEmptyArrays": True}},
    {"$addFields": {"hotel_name": "$_hotel.name", ...}},
    {"$project": {"_hotel": 0, "hotel_oid": 0}},
]
```

All five service functions that previously had N+1 loops now use `$lookup`:
| Function | Joins |
|---|---|
| `get_all_available_food` | hotels |
| `get_foods_by_hotel` | hotels + ngos + volunteers |
| `get_foods_by_region` | hotels |
| `get_foods_by_volunteer` | hotels |

**Performance impact:** For 100 food listings, v2 made up to 300 sequential DB round trips. v3 makes 1 aggregation call regardless of listing count.

---

### 3. APScheduler — food expiry automation

**Files changed/added:**
- `backend/app/scheduler.py` ← NEW
- `backend/app/services/food_service.py` — added `expire_stale_listings()`
- `backend/app/main.py` — starts/stops scheduler on FastAPI lifecycle events

**How it works:**
1. `FoodCreate` schema now accepts `expiry_hours` (float, 0.5–6, default 6).
2. `add_food_listing()` computes `expires_at = utcnow() + timedelta(hours=expiry_hours)` and stores it on the document.
3. APScheduler runs `expire_stale_listings()` every **5 minutes**. That function does a single bulk `update_many`:
   ```python
   await db["foods"].update_many(
       {"status": "available", "expires_at": {"$lte": datetime.utcnow()}},
       {"$set": {"status": "expired"}}
   )
   ```
4. Expired listings disappear from the NGO/volunteer feed immediately on next poll; hotel dashboard shows them greyed out with an "Expired" badge.

**Scheduler config:** `IntervalTrigger(minutes=5)`, single instance (`max_instances=1`), non-blocking shutdown.

---

### 4. Expiry duration picker (Hotel Dashboard)

**File changed:** `frontend/src/pages/HotelDashboard.jsx`

A range slider is shown when adding a new listing:
- Steps: 30 min, 1 hr, 1.5 hr, 2 hr, 3 hr, 4 hr, 5 hr, **6 hr (max)**
- Selected value is sent to the backend as `expiry_hours`.
- Success toast shows "Expires in X hrs/min" confirmation.
- Cards for available listings show "⏰ expires HH:MM" next to quantity.
- Expired cards are greyed out and skip the progress stepper.

---

### 5. Additional hardening (bonus improvements)

- **Duplicate phone guard** on all three registration services — returns HTTP 400 instead of silent duplicate insert.
- **`_oid()` helper** in `food_service.py` — wraps `ObjectId(s)` with a proper HTTP 400 on invalid IDs instead of an unhandled 500.
- **Password never returned** — all service functions call `doc.pop("password", None)` before returning to caller.
- **Expired stat card** in Hotel Dashboard stats row (only shown when count > 0).
- **Volunteer phone** shown in hotel OTP panel when a volunteer (not NGO) claimed the food.

---

## New env vars

| Var | Default | Purpose |
|---|---|---|
| `SECRET_KEY` | `CHANGE_ME_IN_PRODUCTION_…` | JWT signing secret — **must** be changed in prod |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `1440` (24 h) | JWT expiry |

---

## New pip dependencies

```
python-jose[cryptography]==3.3.0   # JWT encode/decode
passlib[bcrypt]==1.7.4              # bcrypt hashing
APScheduler==3.10.4                 # background job scheduler
```

Install: `pip install -r backend/requirements.txt`
