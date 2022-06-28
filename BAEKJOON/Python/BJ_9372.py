# import sys
# input = sys.stdin.readline
#
# T = int(input())
#
# for _ in range(T):
#     N, M = map(int, input().split())
#     edges = []
#     for _ in range(M):
#         edges.append(list(map(int, input().split())))
#
#     print(N-1)
#


import sys
input = sys.stdin.readline

def dfs(node, cnt):
    visited[node] = 1
    for n in graph[node]: # 입력된 노드와 연결된 모든 노드에 대해서
        if visited[n] == 0: # 방문 기록이 없으면
            cnt = dfs(n, cnt+1) # 카운트를 1늘리고 다음 노드 탐색
    return cnt # 연결된 모든 노드에 방문이 되어있는 상태라면

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)] # 각 노드마다 연결된 노드를 저장하는 리스트
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (N+1)
    visited[1] = 0
    cnt = dfs(1,0)
    print(cnt)