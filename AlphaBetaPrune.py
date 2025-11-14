import math

# Game tree as nested dictionaries
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
}

# Leaf values (updated with two values for each node)
values = {
    'H': [41, 5], 'I': [12, 90],
    'J': [101, 80], 'K': [20, 30],
    'L': [34, 80], 'M': [36, 35],
    'N': [50, 36], 'O': [25, 3]
}

def is_leaf(node):
    return node in values


# -------------------------------------------------------------
# PRINT TREE STRUCTURE
# -------------------------------------------------------------
def print_tree(node, indent="", is_last=True):
    """Recursively prints the tree in a hierarchical structure."""
    connector = "└─ " if is_last else "├─ "
    print(indent + connector + node, end="")

    # If leaf: print leaf values
    if is_leaf(node):
        print(f" : {values[node]}")
        return
    else:
        print("")

    children = tree[node]
    for i, child in enumerate(children):
        last = (i == len(children) - 1)
        new_indent = indent + ("   " if is_last else "│  ")
        print_tree(child, new_indent, last)


# -------------------------------------------------------------
# ALPHA-BETA IMPLEMENTATION
# -------------------------------------------------------------
def max_value(node, alpha, beta):
    if is_leaf(node):
        return max(values[node])

    v = -math.inf
    for child in tree[node]:
        v = max(v, min_value(child, alpha, beta))
        if v >= beta:
            return v     # beta cutoff
        alpha = max(alpha, v)
    return v


def min_value(node, alpha, beta):
    if is_leaf(node):
        return min(values[node])

    v = math.inf
    for child in tree[node]:
        v = min(v, max_value(child, alpha, beta))
        if v <= alpha:
            return v     # alpha cutoff
        beta = min(beta, v)
    return v


# -------------------------------------------------------------
# RUN
# -------------------------------------------------------------
print("INITIAL GAME TREE:\n")
print_tree("A")

print("\nRunning Alpha-Beta...\n")
result = max_value('A', -math.inf, math.inf)
print("Root value:", result)
