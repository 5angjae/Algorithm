# BAEKJOON 16988
# 바둑판 총 칸 : 20 * 20 = 400
# 400 * 399 = 159600

from itertools import combinations
from collections import deque

def baduk(ax, ay, bx, by):
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    # 바둑돌 2개 가능한 조합에 두기
    arr[ax][ay] = 1
    arr[bx][by] = 1
    # 위 상태로 뒀을 때 상대의 돌을 총 몇개 잡을 수 있는지 확인
    # 상대의 돌이 있는 좌표에서 bfs를 돌린다.
    # 상대의 돌을 기준으로 bfs를 돌릴 때 0을 만나게 된다면 이는 둘러 싸인 것이 아니다.
    # 2를 만난다면 그 개수를 계속 세면 된다.
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2 and visited[i][j] == 0:
                stone = getStone(i, j, visited)
                if stone != -1:
                    cnt += stone

    # 바둑돌을 다시 원래대로 돌리기
    arr[ax][ay] = 0
    arr[bx][by] = 0

    return cnt

def getStone(x, y, visited):
    queue = deque()
    visited[x][y] = 1
    queue.append([x, y])
    stone = 1
    state = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if arr[nx][ny] == 0: # 0 만나면 둘러싸인 쪽의 돌이 아님 표시.
                    state = 1
                elif arr[nx][ny] == 2: # 2만 계속 찾아서 queue에 넣어서 개수 추가로 세기
                    visited[nx][ny] = 1
                    queue.append([nx,ny])
                    stone += 1
    if state == 1:
        return -1
    else:
        return stone

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

possible_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            possible_list.append([i,j])

possible_comb = list(combinations(possible_list, 2))

answer = 0

for comb in possible_comb:
    ax, ay = comb[0][0], comb[0][1]
    bx, by = comb[1][0], comb[1][1]

    answer = max(answer, baduk(ax,ay,bx,by))

print(answer)