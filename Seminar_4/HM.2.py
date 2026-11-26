import yaml
import matplotlib.pyplot as plt
import math
class Matrix:
    def __init__(self, n, m, arr=None):
        if arr is None:
            self.n = n
            self.m = m
            self.arr = [[0] * m for _ in range(n)]
        else:
            if len(arr) != n:
                raise ValueError('Несовпадение размеров')
            for i in range(n):
                if len(arr[i]) != m:
                    raise ValueError('Несовпадение размеров')
            self.n = n
            self.m = m
            self.arr = arr

    def print_matrix(self):
        for i in range(self.n):
            print('|', *self.arr[i], '|')

    def get_item(self, n_i, m_i):
        return self.arr[n_i-1][m_i-1]
    def set_item(self, n_i, m_i, val):
        self.arr[n_i-1][m_i-1] = val


    def add(self, obj):
        if isinstance(obj, int):
            LE = Matrix(self.n, self.m)
            for i in range(self.n):
                LE.set_item(i+1, i+1, obj)
            ans = Matrix(self.n, self.m)
            for i in range(ans.n):
                for j in range(ans.m):
                    ans.set_item(i+1, j+1, self.arr[i][j] + LE.get_item(i+1, j+1))
            return ans
        elif isinstance(obj, Matrix):
            if obj.n != self.n or obj.m != self.m:
                raise ValueError('Несовпадение размеров')
            ans = Matrix(self.n, self.m)
            for i in range(ans.n):
                for j in range(ans.m):
                    ans.set_item(i+1, j+1, self.arr[i][j] + obj.get_item(i, j))
            return ans
        else:
            raise ValueError('Неверный тип данных')

    def sub(self, obj):
        if isinstance(obj, int):
            ans = Matrix(self.n, self.m)
            for i in range(ans.n):
                for j in range(ans.m):
                    ans.set_item(i+1, j+1, self.arr[i][j] * obj)
            return ans
        elif isinstance(obj, Matrix):
            if self.m != obj.n:
                raise ValueError('Несовпадение размеров')
            ans = Matrix(self.n, obj.m)
            for i in range(ans.n):
                for j in range(ans.m):
                    ans_i = 0
                    for k in range(self.m):
                        ans_i += self.arr[i][k] * obj.get_item(k+1, j+1)
                    ans.set_item(i+1, j+1, ans_i)
            return ans
        else:
            raise ValueError('Неверный тип данных')

    def determinant(self):
        if self.n != self.m:
            raise ValueError('Матрица не квадратная')
        n = self.n
        s = self.arr.copy()
        det = 1
        for column in range(n):
            pivot = max(range(column, n), key=lambda x: abs(s[x][column]))
            if abs(s[pivot][column]) < 1e-12:
                return 0
            if pivot != column:
                s[pivot], s[column] = s[column], s[pivot]
                det = -det
            det *= s[column][column]
            for line in range(column+1, n):
                k = s[line][column] / s[column][column]
                for i in range(column, n):
                    s[line][i] -= k * s[column][i]
        return det

n = int(input())
m = int(input())
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = Matrix(n, m, arr)
A.print_matrix()
print(A.get_item(1, 1))
A.set_item(3, 3, 10)
A.print_matrix()
A = A.add(1)
A.print_matrix()
lst = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
B = Matrix(3, 3, lst)
A = A.add(B)
A.print_matrix()
L = Matrix(2, 3, [[1, 2, 3], [1, 0, -1]])
D = Matrix(3, 3, [[3, 4, 5], [6, 0, -2], [7, 1, 8]])
res = L.sub(D)
res.print_matrix()
N = Matrix(3, 3, [[2, 1, -1], [4, 3, 0], [-2, 5, 2]])
print(N.determinant())

class Oscillator:
    def __init__(self, m=1, k=1, delta=0, x=0, v=1):
        self.m = m
        self.k = k
        self.delta = delta
        self.x = x
        self.v = v
        self.t = 0
    # m x'' = -k*x - c*x'
    # x'' = -2*delta*x' - w^2 * x
    def acceleration(self):
        return (-self.k * self.x - 2 * self.m * self.delta * self.v) / self.m
    def energy(self):
        kin = 0.5 * self.m * self.v**2
        potent = 0.5 * self.k * self.x**2
        return kin + potent
    def step(self, dt):
        def morph(x, v):
            a = (-self.k * x - 2 * self.m * self.delta * v) / self.m
            return v, a
        x, v = self.x, self.v
        k1x, k1v = morph(x, v)
        k2x, k2v = morph(x + 0.5 * dt * k1x, v + 0.5 * dt * k1v)
        k3x, k3v = morph(x + 0.5 * dt * k2x, v + 0.5 * dt * k2v)
        k4x, k4v = morph(x + dt * k3x, v + dt * k3v)
        self.x += dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
        self.v += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        self.t += dt

class Simulator:
    def __init__(self, m=1, k=1, delta=0, x=0, v=1):
        self.body = Oscillator(m, k, delta, x, v)
    def simulate(self, t, dt):
        self.energy_hist = [self.body.energy()]
        self.x_hist = [self.body.x]
        self.v_hist = [self.body.v]
        self.t_hist = [self.body.t]
        steps = math.floor(t // dt)
        for i in range(steps):
            self.body.step(dt)
            self.energy_hist.append(self.body.energy())
            self.t_hist.append(self.body.t)
            self.x_hist.append(self.body.x)
            self.v_hist.append(self.body.v)
    def plot(self):
        fig, ax = plt.subplots(2, 2, figsize=(16, 10))
        fig.suptitle(f"m={self.body.m}, k={self.body.k}, delta={self.body.delta}")

        ax[0, 0].plot(self.t_hist, self.x_hist)
        ax[0, 0].set_title('x(t)'); ax[0, 0].set_ylabel('x'); ax[0, 0].set_xlabel('t')

        ax[0, 1].plot(self.t_hist, self.v_hist)
        ax[0, 1].set_title('v(t)'); ax[0, 1].set_ylabel('v'); ax[0, 1].set_xlabel('t')

        ax[1, 0].plot(self.t_hist, self.energy_hist)
        ax[1, 0].set_title('E(t)'); ax[1, 0].set_ylabel('E'); ax[1, 0].set_xlabel('t')

        ax[1, 1].plot(self.v_hist, self.x_hist)
        ax[1, 1].set_title('x(v)'); ax[1, 1].set_ylabel('x'); ax[1, 1].set_xlabel('v')

        plt.show()

with open('HM2config.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)
s = Simulator(data['oscillator']['m'], data['oscillator']['k'], data['oscillator']['delta'], data['oscillator']['x'], data['oscillator']['v'])
s.simulate(data['simulation']['t'], data['simulation']['dt'])
s.plot()
