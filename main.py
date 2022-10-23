import random
import numpy as np
from numpy import linalg

print("\nРезультат работы программы:")

t = int(input("Введите количество знаков после запятой при вычислении неточности : "))

size = int(input("Введите размерность матрицы: "))
while (size < 1) or (size > 100):
    size = int(input("Неверно!\nВведите размерность матрицы:"))

X = np.random.randint(1, 10, (size, size))
print("Матрица:\n", X)

precision = int(input('Введите количество знаков после запятой в результате вычисления: '))
precision = 0.1**precision

fact = 1
n = 1
summa = 0
delta = 0
frac = 1
while abs(frac) > precision:
    delta += summa
    if n % 2 == 1:
        summa += -1 * ((np.linalg.det(linalg.matrix_power(X, 2 * n + 1))) / fact)
    else:
        summa += 1 * ((np.linalg.det(linalg.matrix_power(X, 2 * n + 1))) / fact)
    n += 1
    fact = fact * (2 * n + 1) * (2 * n + 1)
    frac = delta - summa
    delta = 0
    print(n - 1, ':', summa, ' ', frac)
print('Сумма знакопеременного ряда:', summa)