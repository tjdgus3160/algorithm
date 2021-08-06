import sys

input = sys.stdin.readline

dir = {'U': 0, 'R': 1, 'L': 2, 'D': 3}
dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]


def simulation():
    global arr
    tmp = [[-1] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if arr[y][x] != -1:
                nx = x + dx[arr[y][x]]
                ny = y + dy[arr[y][x]]
                if 0 <= nx < n and 0 <= ny < n:
                    if tmp[ny][nx] == -1:
                        tmp[ny][nx] = arr[y][x]
                    else:
                        tmp[ny][nx] = -2
                else:
                    d = 3 - arr[y][x]
                    if tmp[y][x] == -1:
                        tmp[y][x] = d
                    else:
                        tmp[y][x] = -2
    for y in range(n):
        for x in range(n):
            if tmp[y][x] == -2:
                tmp[y][x] = -1
    arr = tmp


for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [[-1] * n for _ in range(n)]
    for _ in range(m):
        y, x, d = input().split()
        arr[int(y) - 1][int(x) - 1] = dir[d]
    for _ in range(2 * n):
        simulation()
    print(sum([True for y in range(n) for x in range(n) if arr[y][x] != -1]))
