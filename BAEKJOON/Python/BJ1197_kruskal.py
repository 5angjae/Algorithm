# BOJ 1197 최소 스패닝 트리
# 최소 스패닝 트리 : 주어진 그래프의 모든 정점을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# Kruskal
V, E = map(int, input().split())
root_node = [i for i in range(V+1)]
arr = []
for _ in range(E):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[2])

def root(x):
    if x!=root_node[x]:
        root_node[x] = root(root_node[x])
    return root_node[x]

answer = 0
for a, b, c in arr:
    root_a = root(a)
    root_b = root(b)
    if root_a != root_b:
        if root_a > root_b:
            root_node[root_a] = root_b
        else:
            root_node[root_b] = root_a
        answer += c
print(answer)


# Spanning Tree는 트리의 특수한 형태이므로 모든 정점들이 연결되어 있어야 하고
# 사이클을 포함해서는 안된다.
# 따라서 Spanning Tree는 그래프에 있는 n개의 정점을 정확히 (n-1)개의 간선으로 연결한다.
#
# MST는 가중치 합이 최소인 Spanning Tree
#
# MST 구현 방법에는 Kruskal 과 Prim 이 있다.
#
# 1. Kruskal - greedy method를 이용해서 모든 정점을 최소 비용으로 연결하는 최적해 찾는 법
# - 과정
#     그래프의 간선들을 가중치의 오름차순으로 정렬한다.
#     정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
#         가장 낮은 가중치를 먼저 선택하고, 사이클을 형성하는 간선은 제외
#     해당 간선을 현재 MST의 집합에 추가한다.
#
#
# 2. Prim - 시작 정점에서부터 출발하여 Spanning Tree 집합을 단계적으로 확장해나가는 방법
# - 정점 선택을 기반으로 하는 알고리즘
# - 이전 단계에서 만들어진 신장트리를 확장하는 방법
# - 과정
#     시작단계에서는 시작 정점만이 MST 집합에 포함된다.
#     앞 단계에서 만들어진 MST 집합에 인접한 정점들 중, 최소 간선으로 연결된 정점을 선택하여 트리를 확장한다.
#         즉 가장 낮은 가중치를 먼저 선택한다.
#     위 과정을 트리가 N-1 개의 간선을 가질때까지 반복한다.
#
#
# 3. 시간 복잡도
# - Kruskal
#     간선을 정렬하는 시간에 좌우된다. 따라서 간선 e개를 기준으로 했을 때
#     O(elog2e)
# - Prim
#     주 반복문이 정점의 수 n 만큼 반복하고, 내부 반복문이 n번 반복
#     따라서 O(n²)
# - 비교
#     적은 숫자의 간선만을 가지는 '희소그래프(sparse graph)'의 경우 Kruskal 적합
#     간선이 많이 존재하는 '밀집 그래프(dense graph)'의 경우 Prim 적합