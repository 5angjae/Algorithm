#BAEKJOON_1758_알바생_강호

N = int(input())
tips = [int(input()) for _ in range(N)]
minus = [i for i in range(N)]

# 최대한 큰게 앞에 와야함
# 왜냐면 -값이 되는 순간 0이 되니까

tips.sort(reverse=True)

answer = 0
for i in range(N):
    if tips[i] - minus[i] >= 0:
        answer += tips[i] - minus[i]

print(answer)