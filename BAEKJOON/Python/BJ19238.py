# 무조건 최단거리로 이동
# 최단거리의 승객에게 이동 후,
# 그 승객의 목적지로 이동 (이동한 만큼 * 2 만큼 연료 충전)
# 모든 승객을 데려다 주 수 있는가? + 최종적으로 남는 연료의 양
# 데려다 줄 수 없으면 -1 / 데려다 줄 수 있으면 남는 연료 양
from collections import deque

def dist(start, goal, arr):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append(start)
    visited = [[0]*len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                visited[i][j] = -1
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr):
                if visited[nx][ny] == -1:
                    pass
                elif visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                    # print("-----------")
                    # for v in visited:
                    #     print(v)

    return visited[goal[0]][goal[1]]

N, M, F = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))
P_G = [list(map(int, input().split())) for _ in range(M)]
state = 0
new_start = [start[0]-1, start[1]-1]
passenger_info = []
for pg in P_G:
    passenger = [pg[0]-1, pg[1]-1]
    goal = [pg[2]-1, pg[3]-1]
    # print("승객까지 거리", dist(new_start,passenger, arr))
    # print("승객부터 골 까지 거리", dist(passenger,goal, arr))

    passenger_info.append([dist(new_start,passenger, arr), dist(passenger,goal, arr), passenger, goal, pg])
    if dist(new_start, passenger, arr) == 0:
        state =1

while F > 0:
    # print(F)
    if len(P_G) == 0:
        break
    passenger_info.sort(key=lambda x: (-x[0], -x[2][0], -x[2][1]))
    # print("정렬결과", passenger_info)
    p = passenger_info.pop()
    if F - p[0] < 0:
        state = 1
        break
    else:
        if F-p[0]-p[1] < 0:
            state = 1
            break
        else:
            F = F - p[0] + p[1]
            new_start = p[3]
            P_G.remove(p[4])
            passenger_info = []
            # print(new_start)
            for pg in P_G:
                passenger = [pg[0] - 1, pg[1] - 1]
                goal = [pg[2] - 1, pg[3] - 1]
                # print("승객까지 거리", dist(new_start, passenger, arr))
                # print("승객부터 골 까지 거리", dist(passenger, goal, arr))
                passenger_info.append([dist(new_start, passenger, arr), dist(passenger, goal, arr), passenger, goal, pg])

if state == 0:
    print(F)
elif state == 1:
    print(-1)