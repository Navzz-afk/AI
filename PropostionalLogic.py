from itertools import product

def evaluate(expr, model):
    """Evaluate a propositional logic expression under the given truth assignment (model)."""
    if isinstance(expr, str):
        return model[expr]
    op = expr[0]
    if op == 'and':
        return evaluate(expr[1], model) and evaluate(expr[2], model)
    elif op == 'or':
        return evaluate(expr[1], model) or evaluate(expr[2], model)
    elif op == 'not':
        return not evaluate(expr[1], model)
    elif op == 'implies':
        return (not evaluate(expr[1], model)) or evaluate(expr[2], model)
    else:
        raise ValueError(f"Unknown operator: {op}")

def get_symbols(expr):
    """Recursively extract all unique propositional symbols from an expression."""
    if isinstance(expr, str):
        return {expr}
    symbols = set()
    for subexpr in expr[1:]:
        symbols.update(get_symbols(subexpr))
    return symbols

def entails(kb, query):
    """Check if KB entails the query using truth table enumeration and print the table."""
    symbols = sorted(list(get_symbols(kb) | get_symbols(query)))
    print("\nTruth Table:")
    print(" | ".join(symbols + ['KB', 'Query']))
    print("-" * (6 * len(symbols) + 20))

    is_entailed = True

    for values in product([False, True], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        kb_val = evaluate(kb, model)
        query_val = evaluate(query, model)

        row = [str(int(model[s])) for s in symbols] + [str(int(kb_val)), str(int(query_val))]
        print(" | ".join(row))

        # Check if there is a model where KB is true and query is false
        if kb_val and not query_val:
            is_entailed = False
            print("  --> Counterexample found: KB true, Query false!")

    return is_entailed

# -------------------------------
# Define the KB:
# KB: (P → ¬Q) ∧ (Q → P) ∧ (Q ∨ R)
# -------------------------------

kb = ('and',
        ('implies', 'P', ('not', 'Q')),
        ('and',
            ('implies', 'Q', 'P'),
            ('or', 'Q', 'R')
        )
     )

# -------------------------------
# Define Queries
# -------------------------------

query1 = 'R'  # Is R entailed?
query2 = ('implies', 'R', 'P')  # Is R → P entailed?
query3 = ('implies', 'Q', 'R')  # Is Q → R entailed?

# -------------------------------
# Check entailment
# -------------------------------

print("Does KB entail R?")
result1 = entails(kb, query1)
print("Result:", result1)

print("\nDoes KB entail (R → P)?")
result2 = entails(kb, query2)
print("Result:", result2)

print("\nDoes KB entail (Q → R)?")
result3 = entails(kb, query3)
print("Result:", result3)
