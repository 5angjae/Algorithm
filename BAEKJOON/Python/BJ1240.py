from collections import deque
import sys
input = sys.stdin.readline

def distance(x, y):
    queue = deque()
    queue.append([x, 0])
    visited = [0] * (N+1)
    visited[x] = 1

    while queue:
        next, dist = queue.popleft()
        if next == y:
            return dist
        for t in tree[next]:
            if visited[t[0]] == 0:
                visited[t[0]] = 1
                queue.append([t[0], t[1] + dist])



N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    i, j, dist = map(int, input().split())
    tree[i].append([j, dist])
    tree[j].append([i, dist])

for _ in range(M):
    x, y = map(int, input().split())
    print(distance(x, y))