def area(a,b,c):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from tkinter import *
"""
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
plt.hist(positions, bins=40)
plt.title("Гистограмма положений 1000 частиц после 1000 шагов")
plt.xlabel("x(N)")
plt.ylabel("N — число шагов")
plt.grid(True, axis="y")
plt.show()

n3 = np.arange(1, N_steps + 1)
std_emp = np.std(x2, axis=0)
theory = np.sqrt(n3)
plt.figure(figsize=(8, 5))
plt.plot(n3, std_emp, label=r"эмпирическое $sigma(N)$")
plt.plot(n3, theory, "r--", label=r"$sqrt{N}$")
plt.xlabel("N — число шагов")
plt.ylabel(r"$sigma(N)$")
plt.title("Зависимость среднеквадратичного отклонения от N")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
"""

"""
def bin_search(arr, x):
    n = len(arr)
    if x == arr[n//2]:
        return n//2
    elif x < arr[n//2-1]:
        return bin_search(arr[:n//2], x)
    elif x > arr[n//2]:
        return bin_search(arr[n//2+1:], x)
    else:
        return False
s = [1, 3, 5, 7, 9, 10]
x = 3
print(bin_search(s, x))

def bin_search_2(arr, x):
    n = len(arr)
    l = 0
    m = n//2
    r = n
    while arr[m] != x:
        if x < arr[m]:
            r = m
        else:
            l = m + 1
        m = (r + l) // 2
        if (r - l) == 1:
            break
    if arr[m] == x:
        #print(f'x is found at i = {m}')
        return True
    else:
        #print('x is not found')
        return False
print(bin_search_2(s, x))


def LIS_n2(arr):
    n = len(arr)
    dp = [1 for i in range(n)]
    for i in range(1, n):
        max_dp = float('-inf')
        for j in range(0, i):
            if arr[j] < arr[i]:
                if dp[j] > max_dp:
                    max_dp = dp[j]
        dp[i] = 1 + max_dp
    return max(dp)
arr = [2, 3, 1, 4, 6, 5]
print(LIS_n2(arr))

def bin_search_LIS(arr, x):
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

def LIS_nlogn(arr):
    n = len(arr)
    dp = [float('inf') for i in range(n+1)]
    dp[0] = float('-inf')
    res = 0
    for x in arr:
        k = bin_search_LIS(dp, x)
        if dp[k - 1] < x < dp[k]:
            dp[k] = x
            res = max(res, k)

    return res
arr = [i for i in range(20000)]
t = time.time()
print(LIS_n2(arr))
print(time.time()-t)
t = time.time()
print(LIS_nlogn(arr))
print(time.time()-t)

def fast_pow(a, n):
    if n == 1:
        return a
    if n % 2 == 0:
        return fast_pow(a, n // 2)**2
    else:
        return a * fast_pow(a, n - 1)
t = time.time()
print(10**5)
print(time.time()-t)
t = time.time()
print(fast_pow(10, 5))
print(time.time()-t)

class Vector_3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __add__(self, other):
        return Vector_3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, other):
        if isinstance(other, Vector_3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, int):
            return Vector_3D(self.x * other, self.y * other, self.z * other)
    def __rmul__(self, other):
        if isinstance(other, int):
            return Vector_3D(self.x * other, self.y * other, self.z * other)
    def __bool__(self):
        if self.x == 0 and self.y == 0 and self.z == 0:
            return False
        else:
            return True
    def __abs__(self):
        return ((self.x**2 + self.y**2 + self.z**2)**0.5)
v_1 = Vector_3D(x = 1, y = 2, z = 9)
v_2 = Vector_3D(x = 1, y = 2, z = 9)
v_3 = v_1 + v_2
s = v_2 * 3
print(s)
s = 3 * v_2
print(s)
print(abs(s))
"""
def bubble_sort(arr, key=None, comparator=lambda x, y: x < y):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if key is None:
                if comparator(arr[j+1], arr[j]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if comparator(key(arr[j+1]), key(arr[j])):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
#a = ['ab', 'abcs', 'aas', 'at', 'a']
#print(bubble_sort(a,key=lambda x: len(x), comparator=lambda x, y: x > y))

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        tmp = arr[i]
        j = i-1
        while tmp < arr[j] and j >= 0:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr
#a = [5, 3, 2, 1, 6, 8, 4]
#print(insertion_sort(a))

def choice_sort(arr):
    n = len(arr)
    for i in range(n):
        min = float('+inf')
        j_min = None
        for j in range(i, n):
            if arr[j] < min:
                min = arr[j]
                j_min = j
        arr[i], arr[j_min] = arr[j_min], arr[i]
    return arr
#a = [5, 2, 6, 4, 7, 9]
#print(choice_sort(a))

class Stack:
    def __init__(self):
        self.array = []
    def push(self, x):
        self.array.append(x)

    def pop(self):
        return self.array.pop()

    def top(self):
        if self.array:
            return self.array[-1]

        else:
            return None
A = Stack()
A.push(5)
A.push(3)
A.pop()
print(A.top())