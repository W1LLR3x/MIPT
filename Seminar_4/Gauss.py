import numpy as np
import matplotlib.pyplot as plt

np.random.seed()

N_steps = 1000
M = 1000

steps1 = np.random.choice([-1, 1], size=N_steps)
x1 = np.concatenate(([0], np.cumsum(steps1)))
n1 = np.arange(N_steps + 1)

plt.figure(figsize=(10, 5))
plt.plot(n1, x1)
plt.xlabel("N — число шагов")
plt.ylabel("x(N)")
plt.title("Траектория одной частицы (1000 шагов)")
plt.grid(True)
plt.show()

steps2 = np.random.choice([-1, 1], size=(M, N_steps))
x2 = np.cumsum(steps2, axis=1)
positions = x2[:, -1]
plt.figure(figsize=(8, 5))
plt.hist(positions)
plt.title("Гистограмма положений 1000 частиц после 1000 шагов")
plt.xlabel("x(N)")
plt.ylabel("Число частиц")
plt.grid(True, axis="y")
plt.show()

n3 = np.arange(1, N_steps + 1)
std_emp = np.std(x2, axis=0)
theory = np.sqrt(n3)
plt.figure(figsize=(8, 5))
plt.plot(n3, std_emp, label=r"эмпирическое $\sigma(N)$")
plt.plot(n3, theory, "r--", label=r"$\sqrt{N}$")
plt.xlabel("N — число шагов")
plt.ylabel(r"$\sigma(N)$")
plt.title("Зависимость среднеквадратичного отклонения от N")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()