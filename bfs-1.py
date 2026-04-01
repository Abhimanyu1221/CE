def get_next_states(x, y, cap1, cap2):
    states = []

    states.append((cap1, y))

    states.append((x, cap2))

    states.append((0, y))

    states.append((x, 0))

    total = x + y
    if total > cap2:
        jug1 = total - cap2
        jug2 = cap2
    else:
        jug1 = 0
        jug2 = total
    states.append((jug1, jug2))

    total = x + y
    if total > cap1:
        jug1 = cap1
        jug2 = total - cap1
    else:
        jug1 = total
        jug2 = 0
    states.append((jug1, jug2))

    return states


def bfs(cap1, cap2, goal, target_jug):
    queue = [((0, 0), [(0, 0)])]
    visited = []

    while len(queue) > 0:

        state, path = queue.pop(0)     
        x, y = state

        if state in visited:
            continue

        visited.append(state)

        if target_jug == 1 and x == goal:
            return path
        if target_jug == 2 and y == goal:
            return path

        for next_state in get_next_states(x, y, cap1, cap2): 
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None



cap1 = int(input("Enter capacity of Jug1: "))
cap2 = int(input("Enter capacity of Jug2: "))
goal = int(input("Enter goal amount: "))
target_jug = int(input("Enter target jug (1 or 2): "))

result = bfs(cap1, cap2, goal, target_jug)

if result is None:
    print("No solution found!")
else:
    print("\n--- BFS Solution ---")
    step_no = 1
    for step in result:
        print("Step", step_no, "-> Jug1:", step[0], "| Jug2:", step[1])
        step_no = step_no + 1   
