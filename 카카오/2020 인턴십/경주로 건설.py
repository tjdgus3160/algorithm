from collections import deque
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

def solution(board):
    n = len(board)
    dq = deque([[0, 0, -1, 0]])  # x, y, direction, cost
    visited = [[0] * n for _ in range(n)]

    while dq:
        x, y, d, c = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not board[ny][nx]:
                cost = c + (100 if d == i or d == -1 else 600)
                if not visited[ny][nx] or visited[ny][nx] >= cost:
                    dq.append([nx, ny, i, cost])
                    visited[ny][nx] = cost
    return visited[-1][-1]

board=[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
print(solution(board))