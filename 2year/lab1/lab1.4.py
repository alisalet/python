import numpy as np

A=np.random.randint(1,11,(5,5))
B=np.random.randint(1,11,(5,5))
print(f'Матрица А:\n{A}\n\nМатрица В:\n{B}\n')
print(f'Поэлементное произведение А и В:\n{A*B}\n')
print(f'Матричное произведение А на В:\n{np.dot(A,B)}\n')
print(f'Определитель матрицы А:\n{np.linalg.det(A):.2f}\n')
print(f'Транспонированная матрица В:\n{B.T}\n')
try:
    print(f'Обратная матрица для А:\n{np.linalg.inv(A)}\n')
except np.linalg.LinAlgError:
    print('Обратной матрицы для матрицы А не существует :(')
C=A.sum(axis=1).reshape(-1,1)
print(f'Вектор-столбец С:\n{C}\n')
print(f'Решение уравнения А*х=С:\n{np.linalg.solve(A,C)}')