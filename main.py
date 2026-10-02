import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from tkinter import *
import matplotlib.ticker as ticker
from fontTools.diff import color

"""
x = [0,1,2,3,4]
y = [0,2,4,6,8]

# Инициализировать рисунок/Figure
# dpi -- количество пикселей на дюйм в рисунке
# figsize -- пропорции "поля" рисунка
plt.figure(figsize=(8,5), dpi=100)

# Line 1

# Основные возможные аргументы функции plot. По умолчанию необходимы только x и y
#plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')

#нарисуем график первой функции -- 2x
plt.plot(x,y, 'b^--', label='2x')

## Line 2

# С помощью numpy мы можем создавать массив из чисел с определенным интервалом функцией arange. np.linspace(..) делает то же самое, но с целыми числами
x2 = np.arange(0,4.5,0.05)

# Нарисуем часть второго графика как сплошную кривую -- квадрат значений x2
# Поскольку x2 -- массив numpy, мы можем это сделать просто "возведя в квадрат" массив
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')

# Нарисуем часть графика пунктиром. 'r' после x и y означает красный цвет, '--' - рисовку пунктиром
plt.plot(x2[5:], x2[5:]**2, 'r--')

# Добавим заголовок (в fontdict нужен словарь, шрифт должен поддерживаться matplotlib'ом)
plt.title('Our First Graph!', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

# Подпишем оси
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Зададим какие-нибудь корявые "штрихи"/ticks на осях. в эти фунции можно передать любой список
plt.xticks([0,1.12,2.66,3,3.5])
plt.yticks([0,2,4,6,8,10])

# сделаем по этим штрихам сетку
plt.grid()

# функция легенды графика для отображения label'ов графиков
plt.legend()

# Можем сохранить график в высоком качестве
plt.savefig('mygraph.png', dpi=300)

# И вызвать эту функцию чтобы график сразу после отрисовки не пропал, пока мы его не закроем
plt.show()

# принцип настройки схожий, но вместо plt.plot используем plt.bar
labels = ['A', 'B', 'C']
values = [1,4,2]

plt.figure(figsize=(5,3), dpi=100)

bars = plt.bar(labels, values)

plt.savefig('barchart.png', dpi=300)

plt.show()

# создадим два списка чисел от 0 до 49 и составим список S попарных сумм элементов двух списков
# посмотрим распределение получившихся чисел построив гистограмму

x = [i for i in range(50)]
y = [j for j in range(50)]
S = [i + j for i in x for j in y]
print(len(S))
#bins задает количество столбцов гистограммы. если не задать, подберутся автоматически
plt.hist(S, bins = 20)

plt.show()
# получился треугольник с центром около 50
# сложить два равномерных распределения -- самый простой способ получить треугольное распределение

# попробуем сгенерировать случайные числа из нормального распределения и посмотреть, как оно выглядит

# среднее
pos = 0

# параметр отвечающий за разброс
scale = 10

# размер массива случайных чисел (сколько их сгенерируем)
size = 10000

# используем функцию из подраздела random библиотеки numpy и передадим наши параметры
values = np.random.normal(pos, 10, size)

# строим гистограмму с 100 блоков
plt.hist(values, 100)

plt.show()

plt.pie([0.5, 0.5, 0.01], labels = ['No','No, but in orange','Perhaps'])

plt.title('What are the chances that I will wake up early tomorrow?')

plt.show()

fig = plt.figure(figsize=(16, 9))  # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(
    211)  # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(
    212)  # создали Axes ax2 в серии из 2 графиков, поставили на позицию [1,2] -- первый график во второй "строке" графиков

# сгенерируем данные для какой-нибудь гистограммы
values = np.random.normal(0, 10, 1000)

# строим гистограмму с 50 блоками
ax1.hist(values, 50)
ax1.grid()  # делаем сетку на графике ax1

x = [i for i in range(50)]
y = [j ** 1.5 for j in x]

ax2.plot(y, x, 'b.', label='blue dots')
ax2.plot(x, y, 'r--', label='red dashed line')
ax2.set_title('second graph')  # здесь название функции немного отличается от случая, когда мы вызывали напрямую из plt!

ax2.grid()  # делаем сетку на графике ax2
ax2.legend()  # делаем легенду на графике ax2

plt.show()

fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(111) # допустим, больше 1 графика нам не надо

x_measured = [1.01, 2.59, 3.03, 5.40, 7.33]
y_measured = [0.41, 0.84, 1.11, 3.22, 5.00]

#используем встроенный линейный интерполятор чтобы посчитать значения прямой МНК в точках, на которых будем строить нашу прямую
#Поскольку мы хотим прямую, нам достаточно двух точек -- начало и конец прямой
# ВАЖНО! np.interp требует, чтобы список "экспериментальные точки" шли по возрастанию x
# ВАЖНО-2! np.interp это не полноценная МНК!
# Для получения коэффициентов МНК и построения прямой МНК нужно пользоваться np.polyfit(x, y, 1) (см. дальше)
x = [0.5, 9.0]
y = np.interp(x, x_measured, y_measured)

# ставим точки функцией scatter, точки будем ставить крестиком
ax1.scatter(x_measured, y_measured, marker='x')

# поставим кресты погрешностей, linestyle = None, чтобы кресты не соединялись прямыми
ax1.errorbar(x_measured, y_measured, yerr=0.2, xerr = 0.1, color = 'k', linestyle = 'None')

#построим красную прямую МНК
ax1.plot(x,y, 'r')

ax1.grid() # делаем сетку

plt.show()
# для готового графика для лабы по общефизу не хватает только названия, подписанных осей и легенды, но это вы уже умеете
# успехов!
"""
"""
s = input()
l = len(s)
pali = True
mirror = True
mirror_still = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
mirror_world = [['E', '3'], ['J', 'L'], ['S', '2'], ['Z', '5']]

for i in range(l//2):
    if s[i] != s[-i-1]:
        pali = False
    if s[i] in mirror_still:
        if s[i] != s[-i-1]:
            mirror = False
    elif s[i] in [mirror_world[j][0] for j in range(3)]:
        for j in range(3):
            if s[i] == mirror_world[j][0] and s[-i-1] == mirror_world[j][1]:
                break
            else:
                mirror = False
    elif s[i] in [mirror_world[j][1] for j in range(3)]:
        for j in range(3):
            if s[i] == mirror_world[j][1] and s[-i-1] == mirror_world[j][0]:
                break
            else:
                mirror = False
    else:
        mirror = False
if s[l//2] not in mirror_still:
    mirror = False
if pali == False and mirror == False:
    print(f'{s} is not a palindrome')
elif pali == True and mirror == False:
    print(f'{s} is a regular palindrome')
elif pali == False and mirror == True:
    print(f'{s} is a mirrored string')
else:
    print(f'{s} is a mirrored palindrome')
"""

data = pd.read_csv('iris_data.csv')
s_sw = np.array(data.loc[data['Species'] == 'Iris-setosa', 'SepalWidthCm'])
s_sl = np.array(data.loc[data['Species'] == 'Iris-setosa', 'SepalLengthCm'])
vi_sw = np.array(data.loc[data['Species'] == 'Iris-virginica', 'SepalWidthCm'])
vi_sl = np.array(data.loc[data['Species'] == 'Iris-virginica', 'SepalLengthCm'])
ve_sw = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'SepalWidthCm'])
ve_sl = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'SepalLengthCm'])
s_pl = np.array(data.loc[data['Species'] == 'Iris-setosa', 'PetalLengthCm'])
vi_pl = np.array(data.loc[data['Species'] == 'Iris-virginica', 'PetalLengthCm'])
ve_pl = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'PetalLengthCm'])
s_pw = np.array(data.loc[data['Species'] == 'Iris-setosa', 'PetalWidthCm'])
vi_pw = np.array(data.loc[data['Species'] == 'Iris-virginica', 'PetalWidthCm'])
ve_pw = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'PetalWidthCm'])
# SW - SL

plt.title(r"SepalWidthCm -- SepalLengthCm")
plt.ylabel("SL")
plt.xlabel(r"SW")

plt.xlim(1.5, 4.5)
plt.ylim(3, 8)


x_dense = np.linspace(s_sw.min(), s_sw.max(), 200)
cfc = np.polyfit(s_sw, s_sl, 1)
print(cfc[-1])
print('-----------------------')
p = np.poly1d(cfc)
plt.scatter(s_sw, s_sl, color='blue', label='Iris-setosa', marker='^')
plt.plot(x_dense, p(x_dense), 'k--', label='МНК')
# для VI и для VE графики не строю потому что там зависимость получается не очень

x_dense = np.linspace(vi_sw.min(), vi_sw.max(), 200)
cfc = np.polyfit(vi_sw, vi_sl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
# для VI и для VE графики не строю потому что там зависимость получается не очень
plt.scatter(vi_sw, vi_sl, color='red', label='Iris-virginica', marker='s')
plt.plot(x_dense, p(x_dense), 'k--')
x_dense = np.linspace(ve_sw.min(), ve_sw.max(), 200)
cfc = np.polyfit(ve_sw, ve_sl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(ve_sw, ve_sl, color='green', label='Iris-versicolor', marker='o')
plt.plot(x_dense, p(x_dense), 'k--')

plt.legend()
plt.grid(True)
plt.show()

# SL - PL

plt.title(r"SepalLengthCm -- PetalLengthCm")
plt.ylabel("PL")
plt.xlabel(r"SL")
plt.xlim(4, 8)
plt.ylim(0, 7)

x_dense = np.linspace(s_sl.min(), s_sl.max(), 200)
cfc = np.polyfit(s_sl, s_pl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(s_sl, s_pl, color='blue', label='Iris-setosa', marker='^')
plt.plot(x_dense, p(x_dense), 'k--', label='МНК')

x_dense = np.linspace(vi_sl.min(), vi_sl.max(), 200)
cfc = np.polyfit(vi_sl, vi_pl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(vi_sl, vi_pl, color='red', label='Iris-virginica', marker='s')
plt.plot(x_dense, p(x_dense), 'k--')

x_dense = np.linspace(ve_sl.min(), ve_sl.max(), 200)
cfc = np.polyfit(ve_sl, ve_pl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(ve_sl, ve_pl, color='green', label='Iris-versicolor', marker='o')
plt.plot(x_dense, p(x_dense), 'k--')

plt.legend()
plt.grid(True)
plt.show()

# SW - PL

plt.title(r"SepalWidthCm -- PetalLengthCm")
plt.ylabel("PL")
plt.xlabel(r"SW")
plt.xlim(1.5, 5)
plt.ylim(0, 7)

x_dense = np.linspace(s_sw.min(), s_sw.max(), 200)
cfc = np.polyfit(s_sw, s_pl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(s_sw, s_pl, color='blue', label='Iris-setosa', marker='^')
plt.plot(x_dense, p(x_dense), 'k--', label='МНК')

x_dense = np.linspace(vi_sw.min(), vi_sw.max(), 200)
cfc = np.polyfit(vi_sw, vi_pl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(vi_sw, vi_pl, color='red', label='Iris-virginica', marker='s')
plt.plot(x_dense, p(x_dense), 'k--')

x_dense = np.linspace(ve_sw.min(), ve_sw.max(), 200)
cfc = np.polyfit(ve_sw, ve_pl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(ve_sw, ve_pl, color='green', label='Iris-versicolor', marker='o')
plt.plot(x_dense, p(x_dense), 'k--')

plt.legend()
plt.grid(True)
plt.show()

# SW - PW

plt.title(r"SepalWidthCm -- PetalWidthCm")
plt.ylabel("PW")
plt.xlabel(r"SW")
plt.xlim(1.5, 4.5)
plt.ylim(0, 3)

x_dense = np.linspace(s_sw.min(), s_sw.max(), 200)
cfc = np.polyfit(s_sw, s_pw, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(s_sw, s_pw, color='blue', label='Iris-setosa', marker='^')
plt.plot(x_dense, p(x_dense), 'k--', label='МНК')

x_dense = np.linspace(vi_sw.min(), vi_sw.max(), 200)
cfc = np.polyfit(vi_sw, vi_pw, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(vi_sw, vi_pw, color='red', label='Iris-virginica', marker='s')
plt.plot(x_dense, p(x_dense), 'k--')

x_dense = np.linspace(ve_sw.min(), ve_sw.max(), 200)
cfc = np.polyfit(ve_sw, ve_pw, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(ve_sw, ve_pw, color='green', label='Iris-versicolor', marker='o')
plt.plot(x_dense, p(x_dense), 'k--')

plt.legend()
plt.grid(True)
plt.show()

# SL - PW

plt.title(r"SepalLengthCm -- PetalWidthCm")
plt.ylabel("PW")
plt.xlabel(r"SL")
plt.xlim(4, 8)
plt.ylim(0, 3)

x_dense = np.linspace(s_sl.min(), s_sl.max(), 200)
cfc = np.polyfit(s_sl, s_pw, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(s_sl, s_pw, color='blue', label='Iris-setosa', marker='^')
plt.plot(x_dense, p(x_dense), 'k--', label='МНК')

x_dense = np.linspace(vi_sl.min(), vi_sl.max(), 200)
cfc = np.polyfit(vi_sl, vi_pw, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(vi_sl, vi_pw, color='red', label='Iris-virginica', marker='s')
plt.plot(x_dense, p(x_dense), 'k--')

x_dense = np.linspace(ve_sl.min(), ve_sl.max(), 200)
cfc = np.polyfit(ve_sl, ve_pw, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(ve_sl, ve_pw, color='green', label='Iris-versicolor', marker='o')
plt.plot(x_dense, p(x_dense), 'k--')

plt.legend()
plt.grid(True)
plt.show()

# PW - PL

plt.title(r"PetalWidthCm -- PetalLengthCm")
plt.ylabel("PL")
plt.xlabel(r"PW")
plt.xlim(0, 3)
plt.ylim(0, 7)

x_dense = np.linspace(s_pw.min(), s_pw.max(), 200)
cfc = np.polyfit(s_pw, s_pl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(s_pw, s_pl, color='blue', label='Iris-setosa', marker='^')
plt.plot(x_dense, p(x_dense), 'k--', label='МНК')

x_dense = np.linspace(vi_pw.min(), vi_pw.max(), 200)
cfc = np.polyfit(vi_pw, vi_pl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(vi_pw, vi_pl, color='red', label='Iris-virginica', marker='s')
plt.plot(x_dense, p(x_dense), 'k--')

x_dense = np.linspace(ve_pw.min(), ve_pw.max(), 200)
cfc = np.polyfit(ve_pw, ve_pl, 1)
print(cfc[-1])
p = np.poly1d(cfc)
plt.scatter(ve_pw, ve_pl, color='green', label='Iris-versicolor', marker='o')
plt.plot(x_dense, p(x_dense), 'k--')

plt.legend()
plt.grid(True)
plt.show()

"""
N = int(input())
fibs = [0 for i in range(N)]
def fib(N, fibs):
    if N == 0:
        fibs[N] = 0
        return 0
    if N == 1:
        fibs[N] = 1
        return 1
    if fibs[N-1] != 0:
        return fibs[N-1]
    fibs[N-1] = fib(N-1, fibs) + fib(N-2, fibs)
    return fibs[N-1]

t1 = time.time()
print(fib(N, fibs))
t2 = time.time()
print(t2-t1)

def fib_dyn(N):
    dp = [0 for i in range(N+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]
t1 = time.time()
print(fib_dyn(N))
t2 = time.time()
print(t2-t1)

def levenstein(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    dp = [[0 for i in range(l2)] for j in range(l1)]
# dp[i][j] -- сколько действить совершить, чтобы получить из s1[:i] -> s2[:j]
    for i in range(l1):
        dp[i][0] = i
    for j in range(l2):
        dp[0][j] = j
    for i in range(1, l1):
        for j in range(1, l2):
            flag = (s1[i] != s2[j])
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + flag)
    return dp[-1][-1]
print(levenstein('abcaas', 'abdsdaw'))

root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("300x300")  # устанавливаем размеры окна

label = Label(text="Hello")  # создаем текстовую метку
label.pack()  # размещаем метку в окне

root.mainloop()

from tkinter import *


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения. обратите внимание, что к root обращаемся как к глобальной переменной
    print("App closed")


root = Tk()
root.geometry("250x200")

root.title("Hello")
root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()

from tkinter import *
from tkinter import ttk  # подключаем пакет ttk

root = Tk()
root.title("Hello")
root.geometry("250x250")

btn = ttk.Button(text="Click")  # создаем кнопку из пакета ttk
btn.pack()  # размещаем кнопку в окне

root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HELLO")
root.geometry("250x250")

btn = ttk.Button()
btn.pack()
# устанавливаем параметр text
btn["text"] = "Send"
# получаем значение параметра text
btnText = btn["text"]
print(btnText)

root.mainloop()

from tkinter import *


# общий вид функции чтобы рекурсивно вывести информацию обо всех виджетах
# кстати, это хороший пример полиморфизма, поскольку виджеты мы можем передавать разные
def print_info(widget, depth=0):
    widget_class = widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   " * depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth + 1)


root = Tk()
root.title("HELLO")
root.geometry("250x250")

btn = Button(
    text="Click")  # кстати, можем добавить параметр state=["disabled"], что сделает кнопку выключенной, пока мы не изменим параметр 'state'
btn.pack()

root.update()  # обновляем информацию о виджетах после их размещения, иначе это произойдет только с вызовом mainloop

print_info(root)  # получаем всю инфу о root. Поскольку у root есть только один виджет, вызовется информация о нем

root.mainloop()

root = Tk()
root.geometry("500x250")

# функция нажатия на кнопку создает новый
# *args означает, что функция может принимать любое количество переменных.
def callback(*args):
   Label(root, text="Hello World!", font=('Montserrat 20 bold')).pack(pady=4) #обратите внимание, что обращаемся к root как к глобальной переменной
'''
ВАЖНО!
Вы передаете функцию в виджет как объект -- поэтому она пишется здесь без скобок.
Если напишете со скобками, то она вызовется один раз и передаст как команду результат вызова (в нашем случае -- ничего).
Протестируйте это.
'''
btn = Button(root, text="Press Enter", command = callback)
btn.pack(ipadx=50) #ipadx задает размер кнопки по x
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось callback
root.bind('<Return>', callback)
root.mainloop()

from tkinter import *
from tkinter import ttk


# Задаем функцию пересчета. обратите внимание, что к feet и meters мы обращаемся как к глобальным переменным, в общем случае так делать нехорошо
# *args означает, что функция может принимать любое количество переменных. здесь они не используется, поэтому для общности написали так
def calculate(*args):
    try:
        value = float(feet.get())  # используем геттер для объекта StringVal
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)  # используем сеттер для объекта StringVal

    except ValueError:
        pass


# Создадим основное окно приложения
root = Tk()
root.title("Feet to Meters")

'''
Зададим виджет Frame с названием mainframe, который будет содержать элементы нашего интерфейса.
После того, как мы создали его, grid() помещает его в окно приложения. 
columnconfigure/rowconfigure говорит что mainframe должен также расширяться
и занимать все свободное место при изменении размеров окна
'''
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

'''
Первый виджет Entry должен принимать количество футов.

Когда мы создаем виджет, нам нужно указать его родителя.
Это виджет, внутри которого будет размещен новый виджет.
Наша запись и другие виджеты, которые мы вскоре создадим, считаются дочерними элементами mainframe.
Родительский элемент передается в качестве первого параметра при создании экземпляра объекта виджета.

Также мы задали, что наше окно ввода должно иметь ширину под 7 символов.

Также мы создали глобальную переменную feet как textvariable для Entry. Туда будет сохраняться ввод в поле ввода feet_entry.
Когда ввод поменяется, Tkinter автоматически обновит feet. 
Для задания feet используется конструктор по умолчанию для таких переменных -- StringVar()

Tkinter должен знать куда вы хотите поместить виджеты относительно друг друга. 
За это отвечает функция grid. Она помещает содержимое в column (1, 2, or 3) и row (also 1, 2, or 3) окна.
sticky отвечает за то, по какой стороне будет выравнивание. W (west) означает запад, то есть левую сторону ячейки
W,E (west-east) означает и левую и правую сторону одновременно, то есть выравнивание посередине.
В Python определены константы для направлений компаса, поэтому вы можете писать просто W или (W, E).
'''
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

'''
Дальше создаем окно вывода. 
'''
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

'''
По нажатии на кнопку будем выполнять функцию calculate. Поскольку в ней уже прописаны операции напрямую с feet и meters,
то нам не нужно задавать какие-либо аргументы, функция автоматически положит нужное значение в meters и значение в 
определенном выше Label обновится.
'''
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# косметические подписи, обратите внимание на расположение
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# сразу помещает курсор ввода в поле feet_entry
feet_entry.focus()
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось calculate
root.bind("<Return>", calculate)

# циклим наше окно
root.mainloop()

import tkinter as Tkinter
from datetime import datetime

counter = 0
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            # To manage the intial delay.
            if counter == 0:
                display = 'Ready!'
            else:
                tt = datetime.utcfromtimestamp(counter) #используем datetime чтобы перевести counter из простого int в часы-минуты-секунды
                string = tt.strftime('%H:%M:%S')
                display = string

            label['text'] = display

            label.after(1000, count) # каждые 1000мс = 1с увеличиваем счетчик на 1
            counter += 1

    #включаем count
    count()


# стартуем
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# тормозим
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False


# перезагружаемся
def Reset(label):
    global counter
    counter = 0
    # Если reset нажат после stop.
    if not running:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
    # Если reset нажат во время работы таймера.
    else:
        label['text'] = '00:00:00'

root = Tkinter.Tk()
root.title("Stopwatch")

# Если окно будет слишком маленьким, будет сложно нажимать на кнопки, так что зададим minsize.
root.minsize(width=250, height=70)

label = Tkinter.Label(root, text='Ready!', fg='black', font='Montserrat 30 bold')
label.pack()
#создадим Frame, на который поместим кнопки
f = Tkinter.Frame(root)

'''
Помните в предыдущем примере мы говорили, что не получится передать в command функцию с круглыми скобками?
Но как быть, если мы хотим передать функцию, которая принимает какой-то аргумент? В нашем примере это Start и Reset
В данном случае мы можем сохранить **вызов** функции с каким-либо аргументом как отдельную функцию, используя ключевое слово lambda
Таким образом, вызова функции не происходит, а saved_start и saved_reset теперь -- объекты-функции, с фиксированным принимаемым аргументом.

В общем случае лямбда-функции это более мощный инструмент, однако пока мы не будем на этом останавливаться.
'''
saved_start = lambda: Start(label)
saved_reset = lambda: Reset(label)

start = Tkinter.Button(f, text='Start', width=6, command = saved_start)
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command = Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command = saved_reset)

# не забываем разместить Frame и кнопки
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')

root.mainloop()

from random import randint

WIDTH = 300
HEIGHT = 200


class Ball:
    def __init__(self):
        self.R = randint(10, 50) #храним размер, при каждом создании объекта будет выбираться случайно
        self.x = randint(self.R, WIDTH - self.R) # храним положение по x и y
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (10, 10) # это по сути шаг движения шаров. если увеличить -- будут двигаться быстрее
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill="green") # при создании шарика отрисовываем его

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0: # отражение от стенок
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0: # отр
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
    print('Hello World! x=', event.x, 'y=', event.y)

#здесь мы уже привычно обращаемся к balls как к глобальной переменной. На самом деле дело в том, что нам лень писать классы.
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack()
#сделаем так, чтобы нажатие левой кнопки на поле выводило координаты точки, в которую мы нажали
canvas.bind('<Button-1>', click_handler)
balls = [Ball() for i in range(5)]
# делаем шаг перемещения и отрисовки шаров. поскольку mainloop циклит наше приложение, это будет происходить, пока мы не закроем окно
tick()
root.mainloop()

class Cat:
    def __init__(self, age, color):
        self.age = age
        self.color = color
    def meow(self):
        print('meow')
    def get_age(self):
        print(f'cat is {self.age}')
    def set_age(self, age):
        self.age = age
        print(f'cat is now {self.age}')
cat1 = Cat(1, 'red')
print(cat1.age)
print(cat1.color)
cat2 = Cat(2, 'black')
print(cat2.age)
print(cat2.color)
cat1.meow()
cat2.get_age()
cat2.set_age(3)
"""
