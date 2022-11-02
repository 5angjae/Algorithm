# BAEKJOON 16947 서울 지하철 2호선

N = int(input())
edge_count = [0] * (N+1)
graph = [[] for _ in range(N+1)]
infos = []
for _ in range(N):
    a, b = map(int, input().split())
    edge_count[a] += 1
    edge_count[b] += 1
    graph[a].append(b)
    graph[b].append(a)
    infos.append([a,b])
while 1 in edge_count:
    for i in range(1, N+1):
        if edge_count[i] == 1:
            graph[graph[i][0]].remove(i)
            edge_count[graph[i][0]] -= 1
            edge_count[i] = 0
#print(edge_count)
answer = [0] * (N+1)
# for i in range(1, N+1):
#     if edge_count[i] != 0:
#         answer.append(0)
#     else:
temp = [1]
while len(temp) != 0:
    temp = []
    for info in infos:
        #print(edge_count[info[0]], edge_count[info[1]])
        if edge_count[info[0]] != 0 and edge_count[info[1]] != 0:
            answer[info[0]] = 1
            answer[info[1]] = 1
        elif edge_count[info[0]] != 0 and edge_count[info[1]] == 0:
            answer[info[0]] = 1
            answer[info[1]] = answer[info[0]] + 1
        elif edge_count[info[0]] == 0 and edge_count[info[1]] != 0:
            answer[info[1]] = 1
            answer[info[0]] = answer[info[1]] + 1
        else:
            if answer[info[0]] != 0 and answer[info[1]] == 0:
                answer[info[1]] = answer[info[0]] + 1
            elif answer[info[0]] == 0 and answer[info[1]] != 0:
                answer[info[0]] = answer[info[1]] + 1
            elif answer[info[0]] != 0 and answer[info[1]] != 0:
                pass
            else:
                temp.append(info)
    infos = temp
#print(answer)
result = []

for i in range(1, N+1):
    result.append(str(answer[i] - 1))

print(" ".join(result))