# 2217번
w=[]
for _ in range(int(input())):
    w.append(int(input()))
w.sort(reverse=True)
result=0
for i in range(len(w)):
    if result<w[i]*(i+1):
        result=w[i]*(i+1)
print(result)