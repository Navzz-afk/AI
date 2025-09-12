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

def misplaced_tiles(state):
    return sum(1 for i, tile in enumerate(state) if tile != 0 and tile != GOAL_STATE[i])

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

def fix_start_parity(start, goal):
    # If parity differs, swap two tiles (not blank) in start to fix it
    if is_solvable(start, goal):
        return start
    else:
        start_fixed = start.copy()
        # Swap first two tiles that are not zero
        for i in range(len(start_fixed)):
            if start_fixed[i] != 0:
                for j in range(i + 1, len(start_fixed)):
                    if start_fixed[j] != 0:
                        start_fixed[i], start_fixed[j] = start_fixed[j], start_fixed[i]
                        return start_fixed
        return start_fixed

def a_star(start_state):
    frontier = []
    heappush(frontier, (misplaced_tiles(start_state), 0, start_state, []))
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
                h = misplaced_tiles(neighbor)
                heappush(frontier, (g + 1 + h, g + 1, neighbor, path + [state]))
    
    return None

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

if __name__ == "__main__":
    # Your initial start state
    start = [1, 2, 3,
             8, 6, 4,
             0, 7, 5]

    # Fix parity if needed
    start = fix_start_parity(start, GOAL_STATE)
    
    print("Start state after parity fix (if needed):")
    print_state(start)

    if not is_solvable(start, GOAL_STATE):
        print("Puzzle is not solvable even after parity fix (unexpected).")
    else:
        solution = a_star(start)
        if solution:
            print(f"Solution found in {len(solution) - 1} moves:")
            for step in solution:
                print_state(step)
        else:
            print("No solution found.")
