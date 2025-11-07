def is_variable(x):
    return isinstance(x, str) and x[0].islower()

def substitute(term, subst):
    """Apply substitutions to a term."""
    if is_variable(term):
        return substitute(subst[term], subst) if term in subst else term
    elif isinstance(term, tuple):
        return tuple(substitute(t, subst) for t in term)
    return term

def unify(x, y, subst=None):
    """Unify two FOL expressions."""
    if subst is None:
        subst = {}

    x = substitute(x, subst)
    y = substitute(y, subst)

    if x == y:
        return subst

    if is_variable(x):
        if occurs_check(x, y, subst):
            return None
        subst[x] = y
        return subst

    if is_variable(y):
        if occurs_check(y, x, subst):
            return None
        subst[y] = x
        return subst

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y):
            return None
        for xi, yi in zip(x, y):
            subst = unify(xi, yi, subst)
            if subst is None:
                return None
        return subst

    return None

def occurs_check(var, term, subst):
    """Check if var occurs in term (to prevent infinite loops)."""
    term = substitute(term, subst)
    if var == term:
        return True
    if isinstance(term, tuple):
        return any(occurs_check(var, t, subst) for t in term)
    return False


# Example usage:
expr1 = ('P', 'x', ('f', 'y'))
expr2 = ('P', ('f', 'z'), ('f', 'a'))

result = unify(expr1, expr2)
print("Unification result:", result)
