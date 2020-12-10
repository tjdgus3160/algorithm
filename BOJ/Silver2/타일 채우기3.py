# 14852번
f=[1,2,7]
n=int(input())
for i in range(n-2):
    f.append((3*f[-1]+f[-2]-f[-3])%1000000007)
print(f[n])