def solution(arr):
    dic={}
    x,y=0,0
    for i in arr:
        if i=='U':
            if y<5:
                y+=1
                if (x,y,x,y-1) not in dic:
                    dic[(x,y-1,x,y)]=1
        elif i=='D':
            if y>-5:
                y-=1
                if (x,y,x,y+1) not in dic:
                    dic[(x,y+1,x,y)]=1
        elif i=='R':
            if x<5:
                x+=1
                if (x,y,x-1,y) not in dic:
                    dic[(x-1,y,x,y)]=1
        else:
            if x>-5:
                x-=1
                if (x,y,x+1,y) not in dic:
                    dic[(x+1,y,x,y)]=1
    return len(dic)

arr="LLLLRLRLRLL"
print(solution(arr))