branches = ["Main Library", "CSE", "ECE"]
demand = [20, 15, 10]
priority = [1, 2, 3]
available = 30

# Allocate books according to priority
order = sorted(range(3), key=lambda i: priority[i])

allocated = [0, 0, 0]

for i in order:
    if available >= demand[i]:
        allocated[i] = demand[i]
        available -= demand[i]
    else:
        allocated[i] = available
        available = 0

print("Library Resource Distribution")

for i in range(3):
    unmet = demand[i] - allocated[i]
    print(branches[i])
    print("Demand:", demand[i])
    print("Allocated:", allocated[i])
    print("Unmet demand:", unmet)

print("Books remaining:", available)