import tkinter as tk
from tkinter import *
import numpy as np
import math
import matplotlib.pyplot as plt


win = tk.Tk()
win.geometry(f"350x130")
win['bg'] = 'green'
win.title('Расположение')

data = []


def click():
    angle = np.linspace(0, 2 * np.pi, 100)
    a = float(data[3].get())
    b = float(data[4].get())

    a_circle = float(data[0].get())
    b_circle = float(data[1].get())

    radius = float(data[2].get())

    x = radius * np.cos(angle) + float(data[0].get())
    y = radius * np.sin(angle) + float(data[1].get())

    x_lin = np.linspace(a_circle - 5, a_circle + 5, 100)
    y_lin = [0]*100

    for i in range(100):
        y_lin[i] = a * x_lin[i] + b
    figure, axes = plt.subplots(1)

    axes.plot(x, y, x_lin, y_lin)
    d = abs(a*a_circle - 1*b_circle + b) / math.sqrt(a**2 + 1)
    if (d > radius):
        answer_label.config(text = 'Не пересекает')
    if (d < radius):
        answer_label.config(text = 'Пересекает хордой')
    if (d == radius):
        answer_label.config(text = 'Касается в одной точке')
    plt.xlim([a_circle - radius - 5, a_circle + radius + 5])
    plt.ylim([b_circle - radius - 5, b_circle + radius + 5])
    plt.show()

for i in range(5):
    my_entry = Entry(win, width=4)
    my_entry.grid(row=i, column=2, sticky = 'we')
    data.append(my_entry)

my_button = Button(win, text = "Выполнить", command = click)
my_button.grid(row = 5, column = 0, sticky = 'w')

answer_label = Label(win, text='')
answer_label.grid(row = 5, column=0, sticky = 'e')

circle_label_X = Label(win, text = 'Введите отклонение от центра для окружности по оси x: ')
circle_label_X.grid(row = 0, column=0, sticky = 'we')

circle_label_Y = Label(win, text = 'Введите отклонение от центра для окружности по оси y: ')
circle_label_Y.grid(row = 1, column=0, sticky = 'we')

circle_label_R = Label(win, text = 'Введите радиус окружности R: ')
circle_label_R.grid(row = 2, column=0, sticky = 'we')

linear_label_a = Label(win, text = 'Введите коэффициент наклонной a: ')
linear_label_a.grid(row = 3, column=0, sticky = 'we')

linear_label_b = Label(win, text = 'Введите коэффициент b: ')
linear_label_b.grid(row = 4, column=0, sticky = 'we')



win.mainloop()
