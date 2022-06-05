# BJ1719_택배
# 택배 화물이 각 집하장 사이를 오갈때 어떤 경로를 거쳐야 하는가
# 가장 먼저 거쳐야 하는 집하장을 경로표에 저장
n, m = map(int ,input().split())
distances = [[float('inf') for _ in range(n)] for _ in range(n)]
fisrt_node = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    s, e, l = map(int, input().split())
    distances[s-1][e-1] = min(distances[s-1][e-1], l)
    distances[e-1][s-1] = min(distances[e-1][s-1], l)
    fisrt_node[s-1][e-1] = e
    fisrt_node[e-1][s-1] = s

for k in range(n):
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]
                fisrt_node[i][j] = fisrt_node[i][k]

for i in range(n):
    fisrt_node[i][i] = '-'
for row in fisrt_node:
    print(*row)
