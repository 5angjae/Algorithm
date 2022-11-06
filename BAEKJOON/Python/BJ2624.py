#BACKJOON_2624_동전_바꿔주기

T = int(input())
k = int(input())
coins = [[0,0]]
for _ in range(k):
    coins.append(list(map(int, input().split())))


dp = [[0 for _ in range(T+1)] for _ in range(k+1)]
# dp : 각 칸 dp[k][T]는 k
dp[0][0] = 1

for i in range(1, k+1): # 각 코인 종류마다
    p, n = coins[i]
    for j in range(T+1):
        dp[i][j] = dp[i-1][j]
        for m in range(1, n+1):
            if j-m+p >= 0:
                dp[i][j] += dp[i-1][j-m*p]
            else:
                break

print(dp[k][T])