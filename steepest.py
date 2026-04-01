def count_misplaced(state, goal):
    misplaced = 0
    for i in range(len(state)):
        if state[i] != goal[i]:
            misplaced = misplaced + 1
    return misplaced

def get_neighbours(state):
    neighbours = []
    for i in range(len(state) - 1):
        new_state = []
        for b in state:
            new_state.append(b)
        temp           = new_state[i]
        new_state[i]   = new_state[i+1]
        new_state[i+1] = temp
        neighbours.append(new_state)
    return neighbours

def steepest_ascent_hill_climbing(initial, goal):
    current = []
    for b in initial:
        current.append(b)

    step = 0

    while True:
        h = count_misplaced(current, goal)
        print("Step", step, "| State:", current, "| Misplaced:", h)

        if h == 0:
            print("✔ GOAL REACHED in", step, "steps!")
            return

        neighbours = get_neighbours(current)

        best_neighbour = None
        best_h         = h

        for neighbour in neighbours:
            h_neighbour = count_misplaced(neighbour, goal)
            if h_neighbour < best_h:
                best_h         = h_neighbour
                best_neighbour = neighbour

        if best_neighbour is None:
            print("✘ Stuck at local maximum. Final state:", current)
            return

        current = best_neighbour
        step = step + 1

print("Enter initial state (bottom to top, space separated)")
print("Example: C A B")
initial = input().split()

print("Enter goal state (bottom to top, space separated)")
print("Example: A B C")
goal = input().split()

steepest_ascent_hill_climbing(initial, goal)