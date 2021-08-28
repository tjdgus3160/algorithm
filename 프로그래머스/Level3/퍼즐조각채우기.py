from collections import defaultdict, deque

def vaild(nx, ny, arr):
    return 0 <= nx < len(arr) and 0 <= ny < len(arr)

def bfs(x, y, visited, arr):
    dq = deque([[x, y]])
    t, l, b, r = y, x, y, x
    visited[(x, y)] = 1
    cnt = 1
    k = arr[y][x]
    while dq:
        x, y = dq.popleft()
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if vaild(nx, ny, arr) and arr[ny][nx] == k and not visited[(nx, ny)]:
                dq.append([nx, ny])
                visited[(nx, ny)] = 1
                t = min(t, ny)
                l = min(l, nx)
                b = max(b, ny)
                r = max(r, nx)
                cnt += 1
    return [l, t, r,b, cnt]

def rotate(arr):
    n = len(arr)
    m = len(arr[0])
    rotated = [[0] * n for _ in range(m)]
    for y in range(n):
        for x in range(m):
            rotated[x][n - 1 - y] = arr[y][x]
    return rotated

def solution(game_board, table):
    res = 0
    n = len(game_board)
    visit, visit2 = defaultdict(int), defaultdict(int)
    blank, piece = [], []

    for y in range(n):
        for x in range(n):
            if not game_board[y][x] and not visit[(x, y)]:
                blank.append(bfs(x, y, visit, game_board))

            if table[y][x] and not visit2[(x, y)]:
                piece.append(bfs(x, y, visit2, table))

    for l1, t1, r1, b1, cnt1 in blank:
        for l2, t2, r2, b2, cnt2 in piece:
            A=[row[l1:r1+1] for row in game_board[t1:b1+1]]
            B=[row[l2:r2+1] for row in table[t2:b2+1]]
            if cnt1 != cnt2:
                continue
            flag=False
            for _ in range(4):
                n = len(A)
                m = len(A[0])
                B = rotate(B)
                if n != len(B) or m != len(B[0]):
                    continue
                for y in range(n):
                    for x in range(m):
                        if A[y][x] + B[y][x] != 1:
                            break
                        if y==n-1 and x==m-1:
                            flag = True
                            break
                    else:
                        continue
                    break
            if flag:
                res += cnt1
                piece.remove([l2, t2, r2, b2, cnt2])
                break
    return res
