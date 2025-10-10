import random

def generate_board(n):
    """Generate a random board with one queen in each column."""
    return [random.randint(0, n-1) for _ in range(n)]

def compute_conflicts(board):
    """Compute the total number of conflicts (pairs of queens attacking each other)."""
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j]:  # same row
                conflicts += 1
            elif abs(board[i] - board[j]) == abs(i - j):  # same diagonal
                conflicts += 1
    return conflicts

def get_neighbors(board):
    """Generate all neighbors by moving one queen in its column."""
    neighbors = []
    n = len(board)
    for col in range(n):
        for row in range(n):
            if row != board[col]:
                neighbor = board.copy()
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def hill_climbing(n, max_steps=1000):
    """Hill climbing algorithm to solve N-Queens with step printing."""
    current = generate_board(n)
    current_conflicts = compute_conflicts(current)
    
    print(f"Initial state with conflicts = {current_conflicts}:")
    print_board(current)

    for step in range(max_steps):
        if current_conflicts == 0:
            print(f"Goal reached at step {step}!")
            return current  # solution found

        neighbors = get_neighbors(current)
        neighbor_conflicts = [(compute_conflicts(neigh), neigh) for neigh in neighbors]
        min_conflicts, best_neighbor = min(neighbor_conflicts, key=lambda x: x[0])

        print(f"Step {step+1}: conflicts = {min_conflicts}")
        print_board(best_neighbor)

        if min_conflicts >= current_conflicts:
            print("No better neighbor found, local optimum reached.")
            break

        current = best_neighbor
        current_conflicts = min_conflicts

    return None  # no solution found within max_steps

if __name__ == "__main__":
    n = 4
    solution = hill_climbing(n)
    if solution:
        print("Solution found:")
        print_board(solution)
    else:
        print("No solution found with hill climbing.")
