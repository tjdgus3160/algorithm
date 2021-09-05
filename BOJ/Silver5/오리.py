import sys
input=sys.stdin.readline

s='quack'
arr=[]
res=0
for i in input().rstrip():
    if i=='q':
        arr.append('q')
    else:
        for idx,t in enumerate(arr):
            if t[-1]==s[s.index(i)-1]:
                flag=True
                t+=i
                arr[idx]=t
                if t==s:
                    arr.remove(s)
                break
        else:
            print(-1)
            exit()
    res=max(res,len(arr))
print(res if not arr else -1)