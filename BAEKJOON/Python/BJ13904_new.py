# BOJ 13904 과제
# 시간 초과 안나게 개선


N = int(input())

homeworks = []
for _ in range(N):
    d, w = map(int, input().split())
    homeworks.append([d, w])