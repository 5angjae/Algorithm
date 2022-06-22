# BOJ14716 현수막
from collections import deque

def check_word(i, j):
    queue = deque()
    queue.append((i, j))
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < M and 0 <= ny < N and banner[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return visited

M, N = map(int, input().split())

banner = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

count_word = 0

for i in range(M):
    for j in range(N):
        if banner[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            check_word(i, j)
            count_word += 1

print(count_word)