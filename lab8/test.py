from pulp import *

# Визначення функції мети f1
def f1(x1, x2):
    return c1 * x1 + c2 * x2

# Визначення функції мети f2
def f2(x1, x2):
    return d1 * x1 + d2 * x2

# Коефіцієнти функцій мети
c1 = 112
c2 = 252
d1 = 262
d2 = 92

# Вагові коефіцієнти
w1 = 0.5 - 0.005 * 12
w2 = 0.5 + 0.005 * 12

# Ініціалізація моделі
model = LpProblem("Adaptive Convolution", LpMaximize)

# Визначення змінних рішення
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

# Додавання функції мети f1 до моделі
model += w1 * f1(x1, x2)

# Додавання обмежень
model += 0.1 * x1 + 0.2 * x2 <= 10 + 1.2
model += 0.2 * x1 + 0.1 * x2 <= 7 + 1.2
model += 0.2 * x1 + 0.05 * x2 <= 5 + 1.2

# Вирішення моделі
model.solve()

# Отримання оптимального розв'язку
x1_opt = value(x1)
x2_opt = value(x2)

# Визначення значень функцій мети f1 і f2 для оптимального розв'язку
f1_opt = f1(x1_opt, x2_opt)
f2_opt = f2(x1_opt, x2_opt)

# Виведення результатів
print("Optimal Solution:")
print("x1 =", x1_opt)
print("x2 =", x2_opt)
print("f1(x) =", f1_opt)
print("f2(x) =", f2_opt)