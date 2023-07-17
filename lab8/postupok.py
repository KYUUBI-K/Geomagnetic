import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Визначення обмежень
A = [[0.1, 0.2], [0.2, 0.1], [0.2, 0.05]]
b = [11.2, 8.2, 6.2]
bounds = [(0, None), (0, None)]

# Розв'язання функції f1(x)
c1 = [-112, -252]
res1 = linprog(c1, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Розв'язання функції f2(x)
c2 = [-262, -92]
res2 = linprog(c2, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Побудова графіку обмежень
x1 = np.linspace(0, 60, 400)
x2_1 = (11.2 - 0.1 * x1) / 0.2
x2_2 = (8.2 - 0.2 * x1) / 0.1
x2_3 = (6.2 - 0.2 * x1) / 0.05

# Побудова області, що задовольняє всім обмеженням
plt.plot(x1, x2_1, label='0.1x1 + 0.2x2 ≤ 11.2')
plt.plot(x1, x2_2, label='0.2x1 + 0.1x2 ≤ 8.2')
plt.plot(x1, x2_3, label='0.2x1 + 0.05x2 ≤ 6.2')

# Вершини трикутника
vertices = [(17.333333333333336,47.333333333333336), (19.42857142857143, 46.28571428571428), (21.000000000000004,39.99999999999998)]
labels = ['A', 'B', 'C']

# Позначення вершин на графіку
for i, vertex in enumerate(vertices):
    plt.scatter(vertex[0], vertex[1], color='red', zorder=5)
    plt.text(vertex[0], vertex[1], labels[i], fontsize=12, verticalalignment='bottom')

# Виведення результатів
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.grid(True)
plt.title('Feasible Region')
plt.show()

# Виведення результатів розв'язку задачі
print("f1(x) = {:.2f}".format(-res1.fun))
print("x1 = {:.2f}".format(res1.x[0]))
print("x2 = {:.2f}".format(res1.x[1]))
print()
print("f2(x) = {:.2f}".format(-res2.fun))
print("x1 = {:.2f}".format(res2.x[0]))
print("x2 = {:.2f}".format(res2.x[1]))
