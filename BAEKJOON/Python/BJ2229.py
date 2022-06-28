# BJ2229_조 짜기
# 학생들 점수는 나이 순서대로 정렬되어 있는 상태이다.
# 이 후 적당히 순서대로 조를 나눔
# 한 조 내에 최대점수와 최소점수 차이값이 잘짜여진 정도 이고
# 이 합이 최대가 되는 최대값을 구하는 문제

N = int(input())
points = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    for k in range(1, i+2):
        temp = points[i-k+1:i+1]
        if k == i+1:
            k = i
        dp[i] = max(dp[i], dp[i-k] + abs(max(temp) - min(temp)))

print(dp[-1])