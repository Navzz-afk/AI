from copy import deepcopy

# Define goal state
GOAL_STATE = [[1,2,3], [4,5,6], [7,8,0]]

# Moves: up, down, left, right
MOVES = [(-1,0), (1,0), (0,-1), (0,1)]

def is_goal(state):
    return state == GOAL_STATE

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def depth_limited_search(state, depth, limit, visited):
    if is_goal(state):
        return state, depth  # Return state and depth when goal found

    if depth >= limit:
        return None, None

    visited.append(state)

    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result, result_depth = depth_limited_search(neighbor, depth+1, limit, visited)
            if result:
                return result, result_depth

    return None, None

def iterative_deepening_search(initial_state, max_depth=30):
    for depth_limit in range(max_depth):
        visited = []
        result, depth = depth_limited_search(initial_state, 0, depth_limit, visited)
        if result:
            return result, depth
    return None, None

def print_state(state):
    for row in state:
        print(' '.join(str(cell) for cell in row))
    print()

# Example usage
if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [0, 4, 6],
        [7, 5, 8]
    ]

    print("Initial State:")
    print_state(initial_state)

    result, depth = iterative_deepening_search(initial_state)

    if result:
        print(f"Goal State Reached at depth {depth}:")
        print_state(result)
    else:
        print("Goal state not reachable within depth limit.")
