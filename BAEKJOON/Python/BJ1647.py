# BOJ 1647 도시 분할 계획
# 분리하고 최소신장트리?
# 최소신장트리를 만들고, 그중 가장 큰 가중치의 값을 뺀다.
# 크루스칼이 적합할 것 (시간복잡도 prim은 n^2 이기 때문에 n이 100000일때는 적합하지 않다.)

# python & Kruskal = 시간초과
# python & Prim = 시간초과
# pypy & Prim = 시간초과
# pypy & Kruskal = 성공
# pypy VS python????
# 다른 방법이 있나?

def root(x):
    if x!= root_node[x]:
        root_node[x] = root(root_node[x])
    return root_node[x]

V, E = map(int, input().split())
root_node = [i for i in range(V+1)]
arr = [list(map(int, input().split())) for _ in range(E)]
arr.sort(key=lambda x: x[2])

answer = 0
dist = []
for s, e, d in arr:
    root_s = root(s)
    root_e = root(e)
    if root_s != root_e:
        if root_s > root_e:
            root_node[root_s] = root_e
        else:
            root_node[root_e] = root_s
        dist.append(d)
        answer += d

print(answer - dist[-1])

# Prim
# import heapq
#
# V, E = map(int, input().split())
# arr = [[] for _ in range(V+1)]
# for _ in range(E):
#     v1, v2, w = map(int, input().split())
#     arr[v1].append([v2, w])
#     arr[v2].append([v1, w])
#
# queue, weight, cnt = [], 0 ,0 # cnt : 간선이 N-1 개여야 하니까 그만큼 돌리기 위함
# visited = [0] * (V+1)
# heapq.heappush(queue, (0,1))
# dist = []
# while cnt < V:
#     (w, v2) = heapq.heappop(queue)
#     if visited[v2] == 0:
#         visited[v2] = 1
#         weight += w
#         dist.append(w)
#         cnt += 1
#
#         for e in arr[v2]:
#             if not visited[e[0]]:
#                 heapq.heappush(queue, [e[1], e[0]])
#
# print(weight - dist[-1])