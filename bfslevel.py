def get_next_states(x, y, cap1, cap2):
    states = []
    states.append((cap1, y))   # Jug1 fill
    states.append((x, cap2))   # Jug2 fill
    states.append((0, y))      # Jug1 empty
    states.append((x, 0))      # Jug2 empty
    total = x + y
    if total > cap2:
        states.append((total - cap2, cap2))  # Pour jug1 → jug2
    else:
        states.append((0, total))
    if total > cap1:
        states.append((cap1, total - cap1))  # Pour jug2 → jug1
    else:
        states.append((total, 0))
    return states


def bfs(cap1, cap2, goal, target_jug):
    # ✅ Queue mein ab (state, path, LEVEL) teen cheezein hain
    queue = [((0, 0), [(0, 0)], 0)]
    visited = []
    current_level = -1

    while len(queue) > 0:
        state, path, level = queue.pop(0)  # level bhi nikalo

        if state in visited:
            continue
        visited.append(state)

        # ✅ Jab level change ho, tabhi print karo "Level X explore ho raha hai"
        if level != current_level:
            current_level = level
            print(f"\nLevel {current_level}")

        print(f"Jug1={state[0]}, Jug2={state[1]}")

        if target_jug == 1 and state[0] == goal:
            return path
        if target_jug == 2 and state[1] == goal:
            return path

        for next_state in get_next_states(state[0], state[1], cap1, cap2):
            if next_state not in visited:
                # ✅ Har child ko level+1 ke saath queue mein daalo
                queue.append((next_state, path + [next_state], level + 1))

    return None


cap1 = int(input("Enter capacity of Jug1: "))
cap2 = int(input("Enter capacity of Jug2: "))
goal = int(input("Enter goal amount: "))
target_jug = int(input("Enter target jug (1 or 2): "))

result = bfs(cap1, cap2, goal, target_jug)

if result is None:
    print("\nNo solution found!")
else:
    print("\n--- BFS Solution (Final Path) ---")
    for i, step in enumerate(result, 1):
        print(f"Step {i} -> Jug1: {step[0]} | Jug2: {step[1]}")
