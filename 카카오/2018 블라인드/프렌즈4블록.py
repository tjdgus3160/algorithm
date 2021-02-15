def solution(r, c, board):
    res=0
    arr=[]
    for i in board:
        arr.append(list(i))
    while True:
        loc=set()
        for y in range(r-1):
            for x in range(c-1):
                if arr[y][x] != '.' and arr[y][x]==arr[y][x+1]==arr[y+1][x]==arr[y+1][x+1]:
                    loc=loc.union({(x,y),(x+1,y),(x,y+1),(x+1,y+1)})
        if not loc:
            break
        for x,y in loc:
            arr[y][x]='.'
            res+=1
        tmp=[]
        for x in range(c):
            k=[i[x] for i in arr]
            s=[]
            if '.' in k:
                for i in k:
                    if i=='.':
                        s.insert(0,i)
                    else:
                        s.append(i)
                tmp.append(s)
            else:
                tmp.append(k)
        arr=[[i[j] for i in tmp] for j in range(r)]
    return res

r=4
c=5
board=['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
print(solution(r,c,board))