from itertools import combinations

def negate_literal(lit):
    """Negate a single literal like 'P' ↔ '¬P'."""
    return lit[1:] if lit.startswith('¬') else '¬' + lit

def resolve(ci, cj):
    """Resolve two clauses ci and cj (each a frozenset of literals)."""
    resolvents = set()
    for lit in ci:
        comp = negate_literal(lit)
        if comp in cj:
            # Remove complementary literals and combine the rest
            new_clause = (ci - {lit}) | (cj - {comp})
            # Skip tautological clauses like {P, ¬P}
            if not any(negate_literal(l) in new_clause for l in new_clause):
                resolvents.add(frozenset(new_clause))
    return resolvents

def pl_resolution(KB, query):
    """Resolution algorithm for propositional logic."""
    clauses = set(KB)
    neg_query = frozenset({negate_literal(query)})
    clauses.add(neg_query)

    print("Initial clauses:")
    for c in clauses:
        print(" ", set(c))
    print()

    new = set()

    while True:
        pairs = list(combinations(clauses, 2))
        generated = set()

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for r in resolvents:
                print(f"Resolve {set(ci)} and {set(cj)}  ⇒  {set(r) if r else '∅'}")
                if not r:  # Empty clause
                    print("\n✅ Derived empty clause — query is PROVED!")
                    return True
                generated.add(r)

        if not generated - clauses:
            print("\n❌ No new clauses — query CANNOT be proved.")
            return False

        clauses |= generated
        print("\nNew clauses added this round:")
        for c in generated:
            print(" ", set(c))
        print("\n---")

# Example knowledge base and query
KB = [
    frozenset({'¬P', 'Q'}),  # P → Q  →  (¬P ∨ Q)
    frozenset({'¬Q', 'R'}),  # Q → R  →  (¬Q ∨ R)
    frozenset({'P'})         # Fact: P
]
query = 'R'

pl_resolution(KB, query)
