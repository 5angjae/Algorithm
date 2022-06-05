# BJ1719

> 이전 스터디 때 못풀었던 문제를 다시 풀어보았다.

```python
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
```

최단경로 문제.

당시, 스터디 내에 풀이자의 설명에 따라서, 플로이드 워셜을 활용해서 풀었다.

**플로이드 워셜 vs 다익스트라** 에 대해서는 추후에 추가적으로 공부를 진행해야 할 것 같다.

단순히 코드가 간단했기 때문에 플로이드 워셜을 활용했지만, 다익스트라에 대해서도 알고 있어야 할 것 같다.

**풀이 방법**

각 정점 사이에 거리를 저장하는 이중 배열(`distances`)을 만들고, 각 정점 사이에 처음으로 도달하는 정점에 해당하는 이중 배열(`first_node`) 또한 만든다.

각 간선 정보를 받을 때, distances와 first_node에 정보들을 채워주고

모든 정점 사이의 간선에 대해서 (for i (for j)), 중간 다리 정보를 넣어주면서 (for k) 더 짧은 경로를 찾아, 2개의 배열을 갱신해주는 방식을 사용했다.

최종적으로 같은 정점 간의 간선 테이블에는 '-'를 입력시켜줘야 원하는 결과가 나오므로 그렇게 활용했다.



### 이후에 추가로 할 공부

1. 최단경로 알고리즘 02.md 문서 채우기
2. 플로이드 워셜 vs 다익스트라 비교 공부하기