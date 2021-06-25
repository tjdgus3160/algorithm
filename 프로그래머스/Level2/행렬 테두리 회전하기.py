def solution(rows, columns, queries):
    res = []
    arr=[[j+i*columns for j in range(1,columns+1)] for i in range(rows)]
    for y1,x1,y2,x2 in queries:
        tmp=arr[y1-1][x1-1]
        k=tmp

        for y in range(y1-1,y2-1):
            arr[y][x1-1]=arr[y+1][x1-1]
            k=min(k,arr[y][x1-1])

        for x in range(x1-1,x2-1):
            arr[y2-1][x]=arr[y2-1][x+1]
            k=min(k,arr[y2-1][x])

        for y in range(y2-1,y1-1,-1):
            arr[y][x2-1]=arr[y-1][x2-1]
            k=min(k,arr[y][x2-1])

        for x in range(x2-1,x1,-1):
            arr[y1-1][x]=arr[y1-1][x-1]
            k=min(k,arr[y1-1][x])
        arr[y1-1][x1]=tmp
        res.append(k)
        # for i in arr:
        #     print(*i)
        # print()
    return res

rows=3
columns=3
queries=[[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
print(solution(rows,columns,queries))