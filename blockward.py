def a_star_blocks():

    def heuristic(state, goal):
        count = 0
        for i in range(len(state)):
            if i < len(goal):
                for j in range(len(state[i])):
                    if j >= len(goal[i]) or state[i][j] != goal[i][j]:
                        count = count + 1
        return count

    def get_neighbors(state):
        neighbors = []
        for i in range(len(state)):
            if len(state[i]) > 0:
                for j in range(len(state)):
                    if i != j:
                        new_state = []
                        for stack in state:
                            new_state.append(stack[:])
                        block = new_state[i].pop()
                        new_state[j].append(block)
                        neighbors.append(new_state)
        return neighbors

    def state_to_tuple(state):
        result = []
        for stack in state:
            result.append(tuple(stack))
        return tuple(result)

    # User se input lo
    print("=== Blocks World Problem ===\n")
    n = int(input("Kitne stacks hain: "))

    print("\nStart State enter karo:")
    print("(blocks bottom se top order mein, space se alag karo)")
    print("(agar stack empty hai toh sirf Enter dabao)\n")

    start = []
    for i in range(n):
        blocks = input(f"Stack {i} (bottom to top): ").split()
        start.append(blocks)

    print("\nGoal State enter karo:")
    goal = []
    for i in range(n):
        blocks = input(f"Stack {i} (bottom to top): ").split()
        goal.append(blocks)

    print("\n--- Solving ---\n")

    open_list = []
    open_list.append((heuristic(start, goal), start))
    visited = []
    steps = 0

    while open_list:
        open_list.sort(key=lambda x: x[0])
        cost, current = open_list.pop(0)

        if current == goal:
            print(f"Goal Reached in {steps} steps!")
            return

        current_tuple = state_to_tuple(current)
        if current_tuple in visited:
            continue
        visited.append(current_tuple)

        print(f"Step {steps}:")
        for i in range(len(current)):
            print(f"  Stack {i}: {current[i]}")
        print(f"  Heuristic: {cost}\n")
        steps = steps + 1

        for neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                open_list.append((heuristic(neighbor, goal), neighbor))

    print("No solution found!")

a_star_blocks()
