import re

# --------------------------------------------------------------------
# Helper utilities
# --------------------------------------------------------------------

def remove_spaces(s):
    return re.sub(r"\s+", "", s)

def replace_implications(expr):
    # Replace <-> first
    while "<->" in expr:
        expr = re.sub(r"(.*)<->(.*)", r"((\1->\2)&(\2->\1))", expr, count=1)
    # Replace ->
    while "->" in expr:
        expr = re.sub(r"(.*)->(.*)", r"(!\1|\2)", expr, count=1)
    return expr

def push_negation(expr):
    # Push ! inwards using De Morgan repeatedly
    changed = True
    while changed:
        changed = False

        # ¬(A & B) -> (¬A | ¬B)
        new_expr = re.sub(r"!\(([^()]+)&([^()]+)\)", r"(!\1|!\2)", expr)
        if new_expr != expr:
            expr = new_expr
            changed = True

        # ¬(A | B) -> (¬A & ¬B)
        new_expr = re.sub(r"!\(([^()]+)\|([^()]+)\)", r"(!\1&!\2)", expr)
        if new_expr != expr:
            expr = new_expr
            changed = True

        # !!A → A
        new_expr = expr.replace("!!", "")
        if new_expr != expr:
            expr = new_expr
            changed = True

    return expr

def distribute(expr):
    # Distribute OR over AND until CNF
    pattern = r"\(([^()]+)\|\(([^()]+)&([^()]+)\)\)"
    while re.search(pattern, expr):
        expr = re.sub(pattern,
                      r"((\1|\2)&(\1|\3))", expr)

    pattern = r"\(\(([^()]+)&([^()]+)\)\|([^()]+)\)"
    while re.search(pattern, expr):
        expr = re.sub(pattern,
                      r"((\1|\3)&(\2|\3))", expr)

    return expr


# --------------------------------------------------------------------
# MAIN CNF FUNCTION
# --------------------------------------------------------------------
def to_cnf(expr):
    expr = remove_spaces(expr)
    expr = replace_implications(expr)
    expr = push_negation(expr)
    expr = distribute(expr)
    return expr


# --------------------------------------------------------------------
# EXAMPLE
# --------------------------------------------------------------------
formula = "(P->Q)&(R|S)"
print("Input:", formula)
print("CNF:", to_cnf(formula))
