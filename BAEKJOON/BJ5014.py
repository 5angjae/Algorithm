# BJ5014_스타트링크
# F : 고층건물 총 층수
# G : 스타트링크가 있는 곳의 위치
# S : 강호가 현재 있는 층
# U : 위로 U층 가는 버튼
# D : 아래로 D층 가는 버튼
# 참고로 U층 위, D층 아래에 해당 층이 없으면 엘리베이터는 움직이지 않음
# 갈 수 없다면 use the stairs 출력
from collections import deque

def BFS(s):
    q = deque()
    q.append(s)
    visited = [0] * (F + 1)
    visited[s] = 1
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            if 1 <= nx < F+1 and visited[nx] == 0:
                q.append(nx)
                counts[nx] = counts[x] + 1
                visited[nx] = 1

F, S, G, U, D = map(int, input().split())

dx = [U, -D]
# 층 별 도달에 필요한 회수 list : counts
counts = [-1] * (F + 1)
# 출발 지점 counts 0으로 초기화
counts[S] = 0
BFS(S)

if counts[G] == -1:
    print("use the stairs")
else:
    print(counts[G])