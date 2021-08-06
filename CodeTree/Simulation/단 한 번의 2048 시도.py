import sys
input=sys.stdin.readline

def rotate():
    global board
    next_board=[[0]*4 for _ in range(4)]
    for y in range(4):
        for x in range(4):
            next_board[y][x]=board[4-x-1][y]
    board=next_board

def func():
    for y in range(4):
        line = []
        for x in range(4):
            if board[y][x]:
                line.append(board[y][x])
        tmp=[]
        prev = None
        while line:
            v = line.pop()
            if not prev:
                prev = v
                continue
            if prev == v:
                tmp.append(prev * 2)
                prev = None
            else:
                tmp.append(prev)
                prev = v
        if prev:
            tmp.append(prev)
        while len(tmp) < 4:
            tmp.append(0)
        tmp.reverse()
        board[y]=tmp

board=[[*map(int,input().split())] for _ in range(4)]
dir=input().rstrip()
if dir=='R':
    func()
if dir=='L':
    for _ in range(2):
        rotate()
    func()
    for _ in range(2):
        rotate()
if dir=='U':
    rotate()
    func()
    for _ in range(3):
        rotate()
if dir=='D':
    for _ in range(3):
        rotate()
    func()
    rotate()
for i in board:
    print(*i)