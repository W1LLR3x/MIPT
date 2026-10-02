import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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