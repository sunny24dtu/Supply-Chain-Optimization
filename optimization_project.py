pip install pulp pandas
Requirement already satisfied: pulp in /usr/local/lib/python3.12/dist-packages (3.3.0)
Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (2.2.2)
Requirement already satisfied: numpy>=1.26.0 in /usr/local/lib/python3.12/dist-packages (from pandas) (2.0.2)
Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas) (2026.1)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0
                                                                                                                          
from pulp import *

# Supply (warehouses)
supply = {
    "W1": 100,
    "W2": 150
}

# Demand (customers)
demand = {
    "C1": 80,
    "C2": 120,
    "C3": 50
}

# Cost matrix
costs = {
    ("W1", "C1"): 2,
    ("W1", "C2"): 4,
    ("W1", "C3"): 5,
    ("W2", "C1"): 3,
    ("W2", "C2"): 1,
    ("W2", "C3"): 7
}

# Model
model = LpProblem("Supply_Chain_Optimization", LpMinimize)

# Decision variables
routes = LpVariable.dicts("Route", costs, lowBound=0)

# Objective function
model += lpSum(routes[i] * costs[i] for i in costs)

# Supply constraints
for w in supply:
    model += lpSum(routes[(w, c)] for c in demand) <= supply[w]

# Demand constraints
for c in demand:
    model += lpSum(routes[(w, c)] for w in supply) >= demand[c]

# Solve
model.solve()

# Output
print("Status:", LpStatus[model.status])
for v in model.variables():
    print(v.name, "=", v.varValue)

print("Total Cost =", value(model.objective))   




