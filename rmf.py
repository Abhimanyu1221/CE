from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np
import time

# Step 1: Data Input
print("=== Random Forest Classifier ===\n")
n = int(input("Enter number of data points: "))
f = int(input("Enter number of features per point: "))

X = []
Y = []

for i in range(n):
    print(f"\nData point {i+1}:")
    row = []
    skip = False

    for j in range(f):
        val = input(f"  Enter feature {j+1}: ")

        # Step 2: Data Cleaning
        if val == "":
            print("  Missing value! Skipping this row.")
            skip = True
            break

        row.append(float(val))

    if skip:
        continue

    label = input(f"  Enter label (class): ")
    if label == "":
        print("  Missing label! Skipping this row.")
        continue

    X.append(row)
    Y.append(label)

print("\nCleaned Data:")
for i in range(len(X)):
    print(f"  Features: {X[i]}  →  Label: {Y[i]}")
    time.sleep(0.3)

# Step 3: Preprocessing
X = np.array(X)

# Labels string hain toh number mein convert karo
le = LabelEncoder()
Y_encoded = le.fit_transform(Y)  # 'A','B' → 0,1

print("\nPreprocessing Done")
print(f"  Classes found: {list(le.classes_)}")
time.sleep(1)

# Step 4: Training
print("\nTraining Random Forest...")
n_trees = int(input("Enter number of trees (default 100, press Enter): ") or 100)

model = RandomForestClassifier(n_estimators=n_trees, random_state=42)
model.fit(X, Y_encoded)

print(f"\nModel trained with {n_trees} trees!")
time.sleep(1)

# Step 5: Model Info
print("\nFeature Importances (konsa feature zyada important hai):")
for i, importance in enumerate(model.feature_importances_):
    print(f"  Feature {i+1}: {importance:.4f}")
time.sleep(1)

# Step 6: Prediction
print("\nEnter new point to predict:")
new_point = []
for j in range(f):
    val = float(input(f"  Enter feature {j+1}: "))
    new_point.append(val)

prediction_encoded = model.predict([new_point])
prediction_label = le.inverse_transform(prediction_encoded)  # 0,1 → 'A','B'

print(f"\nPredicted Class: {prediction_label[0]}")

# Bonus: probability bhi dikhao
proba = model.predict_proba([new_point])[0]
print("\nConfidence:")
for i, cls in enumerate(le.classes_):
    print(f"  {cls}: {proba[i]*100:.1f}%")