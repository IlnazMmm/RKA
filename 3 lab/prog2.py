import numpy as np
from sklearn.linear_model import LogisticRegression
from random import randrange
from math import ceil, floor

# Загрузка данных из текстового файла
data = np.genfromtxt('данные двумерная модель.txt', skip_header=1)  # Пропустить первую строку с названиями столбцов

# Разделение данных на факторы (x) и зависимую переменную (y)
X = data[:, :-1]  # Первые 6 столбцов
y = data[:, -1]   # Последний столбец

# Создание и обучение модели множественной регрессии
model = LogisticRegression()
model.fit(X, y)

# Вывод коэффициентов регрессии
print("Коэффициенты регрессии:")
print("a1, a2:", [round(x, 3) for x in model.coef_[0]])
print("b (пересечение):", round(model.intercept_[0], 3))

X_min = [float('inf'), float('inf')]
X_max = [float('-inf'), float('-inf')]
for x in X:
    for i in range(len(x)):
        if x[i] < X_min[i]:
            X_min[i] = x[i]
        if x[i] > X_max[i]:
            X_max[i] = x[i]

R_X = []
for i in range(len(X_min)):
    R_X.append(randrange(ceil(X_min[i]), floor(X_max[i])))

print(R_X)

# Спрогнозировать новое значение y на основе заданных факторов (замените значения x_new)
x_new = np.array([R_X])
y_pred = model.predict(x_new)
print(f"Прогнозное значение y для новых данных: {y_pred[0]:.2f}")


print(f'{model.coef_[0][0]:.3f} {model.coef_[0][1]:.3f}, {model.intercept_[0]:.3f}')