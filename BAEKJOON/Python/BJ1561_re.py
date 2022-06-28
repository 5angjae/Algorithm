# BJ1561_놀이공원
# 20211123 / 20211221 두번 나온 문제
# 당시 힌트
# 1. 이분탐색을 통해서 아이들을 모두 태울 수 있는 시간을 찾는다.
# 2. 구한 시간 - 1분까지 몇명의 아이들을 태울 수 있는지 탐색한다.

N, M = map(int, input().split())
time_list = list(map(int, input().split()))
# N : 아이들 숫자
# M : 놀이기구 숫자

if N < M:
    print(N)
else:
    l, r = 0, 60000000000 # 최대 아이들 수 2000000000 * 최대 운행시간 30 으로 최대값
    t = None
    while l <= r:
        mid = (l+r)//2
        cnt = M
        for i in range(M):
            cnt += mid//time_list[i] ## 왜 이렇게 하는지 알아야 한다.
        if cnt >= N:
            t = mid
            right = mid - 1
        else:
            left = mid + 1

    for i in range(M):
        if t % time_list[i] == 0:
            cnt += 1
        if cnt == N:
            print(i+1)
            break