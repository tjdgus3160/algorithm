# 20436번
import sys
input=sys.stdin.readline

ja='qwertasdfgzxcv'
mo='yuiophjklbnm'

arr=['qwertyuiop','asdfghjkl','zxcvbnm']

s,r=input().split()
left=[0,0]
right=[0,0]
for y in range(3):
    for x in range(len(arr[y])):
        if arr[y][x] == s:
            left = [x, y]
        if arr[y][x] == r:
            right = [x,y]
res=0
for i in input().rstrip('\n'):
    loc=[0,0]
    for y in range(3):
        for x in range(len(arr[y])):
            if arr[y][x]==i:
                loc=[x,y]
                break
    if i in ja:
        res+=abs(left[0]-loc[0])+abs(left[1]-loc[1])
        left=loc
    else:
        res+=abs(right[0]-loc[0])+abs(right[1]-loc[1])
        right=loc
    res+=1
print(res)