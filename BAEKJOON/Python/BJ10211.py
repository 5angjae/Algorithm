# BJ10211_Maximum Subarray
T = int(input())

for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    max_sub = 0
    dp = [0] * N # 해당 인덱스를 마지막 숫자로 갖는 부분합
    dp[0] = X[0]
    for i in range(1, N):
        dp[i] = max(dp[i-1] + X[i], X[i])
    print(max(dp))