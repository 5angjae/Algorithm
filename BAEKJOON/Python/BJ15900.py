# BJ15900_나무 탈출
N = int(input())

connect_nodes = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    connect_nodes[a].append(b)
    connect_nodes[b].append(a)

stack = [[1, 0]]
visited = [0] * (N+1)

total_len = 0

while stack:
    m_node, l = stack.pop()
    visited[m_node] = 1

    for s_node in connect_nodes[m_node]:
        if visited[s_node] == 0:
            stack.append([s_node, l+1])
    
    if m_node != 1 and len(connect_nodes[m_node]) == 1:
        total_len += l

if total_len % 2:
    print('Yes')
else:
    print('No')