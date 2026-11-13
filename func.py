def area(a,b,c):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from tkinter import *


def bin_search(arr, x):
    n = len(arr)
    if n == 0:
        return False
    elif n == 1:
        return arr[0] == x
    elif x == arr[n//2]:
        return n//2
    elif x < arr[n//2-1]:
        return bin_search(arr[:n//2], x)
    elif x > arr[n//2]:
        return bin_search(arr[n//2+1:], x)
s = [1, 3, 5, 7, 9, 10]
x = 10
#print(bin_search(s, x))
"""
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

"""
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
"""
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


import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 50.5e-2
s_l = 1e-3

a1, b1 = 2.196e-2, 3.849e-3
sa1, sb1 = 1e-3, 1e-6

M1U = np.array([463.6, 935.9, 1397.7, 1899.7, 2402.7,
                 2402.7, 1899.7, 1397.7, 935.9, 463.6]) * 1e-3
y1U = np.array([0.64, 1.74, 2.91, 4.19, 5.03, 5.2,
                 4.15, 2.96, 1.9, 0.69]) * 1e-3

M1D = np.array([463.6, 935.9, 1397.7, 1899.7, 2402.7,
                 2402.7, 1899.7, 1397.7, 935.9, 463.6]) * 1e-3
y1D = np.array([1.02, 2.23, 3.32, 4.65, 5.5, 5.6,
                 4.65, 3.4, 2.27, 1.15]) * 1e-3

a2,  b2    = 2.095e-2, 3.759e-3
sa2, sb2 = 1e-3, 1e-6

M2U = np.array([463.6, 935.9, 1397.7, 1899.7, 2402.7,
                 2402.7, 1899.7, 1397.7, 935.9, 463.6]) * 1e-3
y2U = np.array([0.6, 1.25, 1.85, 2.60, 3.18,
                 3.24, 2.60, 1.9, 1.33, 0.68]) * 1e-3

M2_5 = np.array([463.6, 935.9, 1397.7, 1899.7, 2402.7,
                 2402.7, 1899.7, 1397.7, 935.9, 463.6]) * 1e-3
y2_5 = np.array([0.42, 1.28, 1.9, 2.64, 3.24,
                     3.23, 2.43, 1.91, 1.29, 0.46]) * 1e-3

def lsq(x, y):
    N = len(x)
    xm = x.mean()
    ym = y.mean()
    k = (np.mean(x*y) - xm*ym) / (np.mean(x) - xm)
    b = ym - k * xm
    res = y - (k*x + b)
    s2 = np.sum(res**2) / (N - 2)
    sk = np.sqrt(s2 / (N * (np.mean(x) - xm)))
    return k, b, sk

def you(k, sk, a, b, s_a, s_b):
    E = k * l**3 / (4 * a * b**3)
    sE = E * np.sqrt(
        (sk/k)*2 + (3*s_l/l)*2 + (s_a/a)*2 + (3*s_b/b)*2
    )
    return E, sE

for name, M, y, a, b, s_a, s_b in [
    ('1U', M1U, y1U, a1, b1, sa1, sb1),
    ('1D', M1D, y1D, a1, b1, sa1, sb1),
    ('2U', M2U, y2U, a2, b2, sa2, sb2),
    ('2.5', M2_5, y2_5, a2, b2, sa2, sb2),
]:
    P = M * g
    k, b0, sk = lsq(y, P)
    E, sE = you(k, sk, a, b, s_a, s_b)
    print(name, 'k =', k, 'sk =', sk, 'b =', b0,
          'E =', E/1e9, 'sE =', sE/1e9, 'eps =', 100*sE/E)

for name, M, y in [('1A', M1U, y1U), ('1B', M1D, y1D),
                   ('2A', M2U, y2U), ('2.5', M2_5, y2_5)]:
    P = M * g
    k, b0, sk = lsq(y, P)
    plt.figure(figsize=(9, 6))
    plt.plot(y*1e3, P, 'r^')
    plt.plot(y*1e3, k*y + b0, 'g-')
    plt.xlabel('y_max, мм')
    plt.ylabel('P, Н')
    plt.grid(alpha=.3)
    plt.savefig(f'plot131_{name}.png', dpi=150)


plt.show()
"""