p=[]
j=[]
for _ in range(3):
    p.append(int(input()))
for _ in range(2):
    j.append(int(input()))
p.sort()
j.sort()
a=(p[0]+j[0])*1.1
print("%.1f"%(a))
