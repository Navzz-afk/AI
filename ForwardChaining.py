def forward_chaining(KB, query):
    inferred = set()          # Facts we already know
    new_inferred = True

    while new_inferred:
        new_inferred = False
        for rule in KB:
            # Separate rule into premise and conclusion
            if '=>' in rule:
                premise, conclusion = rule.split('=>')
                premise = [p.strip() for p in premise.split('&')]
                conclusion = conclusion.strip()

                # If all premises are true, infer conclusion
                if all(p in inferred for p in premise):
                    if conclusion not in inferred:
                        print(f"Inferred: {conclusion}")
                        inferred.add(conclusion)
                        new_inferred = True
                        if conclusion == query:
                            print("✅ Query proved!")
                            return True
            else:
                # Atomic fact
                fact = rule.strip()
                if fact not in inferred:
                    inferred.add(fact)

    print("❌ Query cannot be proved.")
    return False


# Example KB
KB = [
    "Rainy",
    "Rainy => Wet",
    "Wet => Slippery"
]

query = "Slippery"

forward_chaining(KB, query)
