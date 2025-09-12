from heapq import heappush, heappop

GOAL_STATE = [1, 2, 3,
              8, 0, 4,
              7, 6, 5]

MOVES = {
    'up': -3,
    'down': 3,
    'left': -1,
    'right': 1
}

def manhattan_distance(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = GOAL_STATE.index(tile)
        current_row, current_col = divmod(i, 3)
        goal_row, goal_col = divmod(goal_index, 3)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_neighbors(state):
    neighbors = []
    blank_index = state.index(0)
    row, col = divmod(blank_index, 3)
    
    for move, delta in MOVES.items():
        new_index = blank_index + delta
        if move == 'left' and col == 0:
            continue
        if move == 'right' and col == 2:
            continue
        if move == 'up' and row == 0:
            continue
        if move == 'down' and row == 2:
            continue
        
        new_state = state.copy()
        new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
        neighbors.append(new_state)
    return neighbors

def count_inversions(state):
    tiles = [tile for tile in state if tile != 0]
    inversions = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1
    return inversions

def is_solvable(start, goal):
    return count_inversions(start) % 2 == count_inversions(goal) % 2

def a_star(start_state):
    frontier = []
    heappush(frontier, (manhattan_distance(start_state), 0, start_state, []))
    explored = set()
    
    while frontier:
        f, g, state, path = heappop(frontier)
        state_tuple = tuple(state)
        
        if state == GOAL_STATE:
            return path + [state]
        
        if state_tuple in explored:
            continue
        explored.add(state_tuple)
        
        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in explored:
                h = manhattan_distance(neighbor)
                heappush(frontier, (g + 1 + h, g + 1, neighbor, path + [state]))
    
    return None

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

if __name__ == "__main__":
    start = [2, 1, 3,
             4, 0, 6,
             7, 5, 8]

    if not is_solvable(start, GOAL_STATE):
        print("Puzzle is not solvable from this start state to the goal state.")
    else:
        solution = a_star(start)
        if solution:
            print(f"Solution found in {len(solution) - 1} moves:")
            for step in solution:
                print_state(step)
        else:
            print("No solution found.")
