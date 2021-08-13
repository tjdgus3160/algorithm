n=int(input())
dot=[[*map(int,input().split())] for _ in range(n)]
tmp=[[abs(x)+abs(y),idx+1] for idx,[x,y] in enumerate(dot)]
tmp.sort()
for i in tmp:
    print(i[1])