def fe_table(n):
    f = {1 : 1}
    for k in range(2, n + 1):
        m = k // 2
        r = k % 2
        l = m % 2
        if (r == 0):
            if (l == 0):
                f[k] = f[m]
            else:
                f[k] = 2 * f[m]
        else:
            if (l == 0):
                f[k] = 2 * f[m] + 1
            else:
                f[k] = f[m]
    return f

N = 2021

ans = 0
f = fe_table(N)
for j in f:
    ans += (f[j] == f[2021])
    
ans -= 1
                