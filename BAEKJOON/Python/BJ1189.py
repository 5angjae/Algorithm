def dfs(x, y, cnt, visited):
    # visited.append([x, y])
    if x == 0 and y == C-1:
        if cnt in cnt_dict:
            cnt_dict[cnt] += 1
        else:
            cnt_dict[cnt] = 1
        return

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and map_info[nx][ny] != 'T' and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            # print(visited)
            dfs(nx, ny, cnt+1, visited)
            visited[nx][ny] = 0
            #dfs(nx, ny, cnt + 1, visited + [nx, ny])

R, C, K = map(int, input().split())
map_info = [list(input()) for _ in range(R)]
cnt_dict = {}

visited = [[0] * C for _ in range(R)]
visited[R-1][0] = 1
dfs(R-1, 0, 1, visited)

if K in cnt_dict:
    print(cnt_dict[K])
else:
    print(0)