# BOJ17404 RGB거리 2
INF = 1000001
N = int(input())
rgb = []
ans = INF
for _ in range(N):
    rgb.append(list(map(int, input().split())))

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][i] = rgb[0][i]
    for j in range(1, N):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)



#
# N = int(input())
# cost_input = [list(map(int, input().split())) for _ in range(N)]
#
# # i집이 j 컬러를 선택했을 때 최소비용 C[i][j]
# # C[i][j] = min(C[i-1][k] + costs[i][j] , C[i-1][l] + costs[i][j])
#
# costs = [cost_input[N-1]] + cost_input[:N-1]
# #print(costs)
# C = [[0] * 3 for _ in range(N)]
# C[0][0] = costs[0][0]
# C[0][1] = costs[0][1]
# C[0][2] = costs[0][2]
# route = [[[] for _ in range(3)] for _ in range(N)]
# route[0][0].append(0)
# route[0][1].append(1)
# route[0][2].append(2)
#
# for i in range(1, N):
#     if C[i - 1][1] + costs[i][0] > C[i - 1][2] + costs[i][0]:
#         route[i][0] = route[i-1][2]
#         C[i][0] = C[i - 1][2] + costs[i][0]
#     elif C[i - 1][1] + costs[i][0] < C[i - 1][2] + costs[i][0]:
#         route[i][0] = route[i-1][1]
#         C[i][0] = C[i - 1][1] + costs[i][0]
#     else:
#         route[i][0] = route[i-1][2] + route[i-1][1]
#         C[i][0] = C[i - 1][1] + costs[i][0]
#
#
#     if C[i - 1][0] + costs[i][1] > C[i - 1][2] + costs[i][1]:
#         route[i][1] = route[i-1][2]
#         C[i][1] = C[i - 1][2] + costs[i][1]
#     elif C[i - 1][0] + costs[i][1] < C[i - 1][2] + costs[i][1]:
#         route[i][1] = route[i-1][0]
#         C[i][1] = C[i - 1][0] + costs[i][1]
#     else:
#         route[i][1] = route[i-1][2] + route[i-1][0]
#         C[i][1] = C[i - 1][0] + costs[i][1]
#
#
#     if C[i - 1][0] + costs[i][2] > C[i - 1][1] + costs[i][2]:
#         route[i][2] = route[i-1][1]
#         C[i][2] = C[i - 1][1] + costs[i][2]
#     elif C[i - 1][0] + costs[i][2] < C[i - 1][1] + costs[i][2]:
#         route[i][2] = route[i-1][0]
#         C[i][2] = C[i - 1][0] + costs[i][2]
#     else:
#         route[i][2] = route[i-1][1] + route[i-1][0]
#         C[i][2] = C[i - 1][0] + costs[i][2]
#
# result = 1000
# for i in range(3):
#     if len(route[N-1][i]) == 1 and route[N-1][i][0] == i:
#         #print(C[N-1][i])
#         pass
#     else:
#         #print(route[N-1][i][0], i)
#         result = min(result, C[N-1][i])
#
# #print(C, route)
# print(result)