"""
The function f is defined on the positive integers as follows:
    f(1) = 1
    f(2n) = f(n) if n is even
    f(2n) = 2f(n) if n is odd
    f(2n + 1) = 2f(n) + 1 if n is even
    f(2n + 1) = f(n) if n is odd
Find the number of positive integers n such that n < 2021 and f(n) = f(2021).
"""

def fe_table(n):
    f = {1 : 1}
    for k in range(2, n + 1):
        m = k // 2
        r = k % 2
        l = m % 2
        f[k] = ((r ^ l) + 1) * f[m] + r * (1 - l)
    return f

N = 2021

ans = -1
f = fe_table(N)
for j in f:
    ans += (f[j] == f[N])                