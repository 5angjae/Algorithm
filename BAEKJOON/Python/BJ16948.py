from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

start = [r1, c1, 0]
queue = deque()
queue.append(start)
answer = -1

board = [[0] * N for _ in range(N)]
board[r1][c1] = 1
while queue:
    s = queue.popleft()

    if s[0] == r2 and s[1] == c2:
        answer = s[2]
        break

    for i in range(6):
        nx = s[0] + dx[i]
        ny = s[1] + dy[i]

        if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
            queue.append([nx, ny, s[2] + 1])
            board[nx][ny] = 1


print(answer)

