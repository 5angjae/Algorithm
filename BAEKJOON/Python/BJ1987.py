# DFS 시간초과

import copy

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
#visited = [[0]*C for _ in range(R)]
stack = []
stack.append((0,0,1,[arr[0][0]], [(0,0)]))
max_cnt = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
while stack:
    x, y, cnt, visit_alpha, visit_position = stack.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<C and 0<=ny<R and arr[ny][nx] not in visit_alpha and (nx, ny) not in visit_position:
            new_visit_al = copy.deepcopy(visit_alpha)
            new_visit_po = copy.deepcopy(visit_position)
            new_visit_al.append(arr[ny][nx])
            new_visit_po.append((nx,ny))
            stack.append((nx,ny,cnt+1, new_visit_al, new_visit_po))
            # visited[ny][nx] = 1
    # print(x, y, cnt, visit_alpha, visit_position)
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)