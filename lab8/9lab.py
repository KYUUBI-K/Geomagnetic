import numpy as np
from scipy.optimize import linprog

# Coefficients for the criteria
c1 = np.array([112, 252])
c2 = np.array([262, 92])

# Constraints
A = np.array([[0.1, 0.2],
              [0.2, 0.1],
              [0.2, 0.05]])
b = np.array([11.2, 8.2, 6.2])
bounds = [(0, None), (0, None)]

# Solve for the first criterion
res2 = linprog(-c2, A_ub=A, b_ub=b, bounds=bounds)
x2_opt = res2.x
f2_opt = -res2.fun

print("Optimization result for the first criterion:")
print(res2)
# Print the final results
print("Optimal x values for the first criterion:", x2_opt)
print("Objective value for the first criterion:", f2_opt)

