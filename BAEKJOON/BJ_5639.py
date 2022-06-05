import sys
sys.setrecursionlimit(10**6)
# 재귀를 사용해서 풀어야 하는 문제의 경우,
# 파이썬의 기본 재귀 깊이 제한을 늘려줌
# 기존 1000 -> 10^6

num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

