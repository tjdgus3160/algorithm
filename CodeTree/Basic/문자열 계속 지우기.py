s=input().rstrip()
t=input().rstrip()
while True:
    idx=s.find(t)
    if idx==-1:
        break
    s=s[:idx]+s[idx+len(t):]
print(s)