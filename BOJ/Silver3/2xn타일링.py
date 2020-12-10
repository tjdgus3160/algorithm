# 11726번
f=[1,1,2]
n=int(input())
for i in range(n-2):
    f.append(f[-1]+f[-2])
print(f[n]%10007)