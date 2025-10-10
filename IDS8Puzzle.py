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

def print_state(state):
    for row in state:
        print(' '.join(str(cell) for cell in row))
    print()

def depth_limited_search(state, depth, limit, visited, path):
    print(f"Exploring state at depth {depth}:")
    print_state(state)

    if is_goal(state):
        return path + [state], depth  # Return full path and depth

    if depth >= limit:
        return None, None

    visited.append(state)

    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result_path, result_depth = depth_limited_search(neighbor, depth+1, limit, visited, path + [state])
            if result_path:
                return result_path, result_depth

    return None, None

def iterative_deepening_search(initial_state, max_depth=30):
    for depth_limit in range(max_depth):
        print(f"Depth Limit: {depth_limit}")
        visited = []
        result_path, depth = depth_limited_search(initial_state, 0, depth_limit, visited, [])
        if result_path:
            return result_path, depth
    return None, None

# Example usage
if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [0, 4, 6],
        [7, 5, 8]
    ]

    print("Initial State:")
    print_state(initial_state)

    result_path, depth = iterative_deepening_search(initial_state)

    if result_path:
        print(f"Goal State Reached at depth {depth}. Path length: {len(result_path)}")
        print("Path to goal:")
        for idx, state in enumerate(result_path):
            print(f"Step {idx}:")
            print_state(state)
    else:
        print("Goal state not reachable within depth limit.")
