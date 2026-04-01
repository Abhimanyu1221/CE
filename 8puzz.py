def heuristic(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


def astar(start, goal):
    open_list = []
    closed_list = []

    open_list.append((start, 0, heuristic(start, goal), []))

    while len(open_list) > 0:

        best_index = 0
        best_f = open_list[0][1] + open_list[0][2]

        for i in range(len(open_list)):
            f = open_list[i][1] + open_list[i][2]
            if f < best_f:
                best_f = f
                best_index = i

        current, g, h, path = open_list.pop(best_index)

        if current == goal:
            return path + [current]

        closed_list.append(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed_list:
                continue

            new_g = g + 1
            new_h = heuristic(neighbor, goal)

            open_list.append((neighbor, new_g, new_h, path + [current]))

    return None


# 🔥 USER INPUT PART
print("Enter Start State (3 rows, space separated):")
start = []
for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

print("Enter Goal State (3 rows, space separated):")
goal = []
for i in range(3):
    row = list(map(int, input().split()))
    goal.append(row)


# ▶️ RUN
result = astar(start, goal)

# 📌 OUTPUT
if result:
    step = 1
    for state in result:
        print("Step", step)
        for row in state:
            print(row)
        print()
        step += 1
else:
    print("No solution found")