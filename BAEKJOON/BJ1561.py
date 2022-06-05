# BJ1561_놀이 공원
def get_min_idx(times):
    min_time = 31
    min_idx = 0
    for idx in range(len(times)):
        if min_time > times[idx]:
            min_idx = idx
            min_time = times[idx]

    return min_idx
        


N, M = map(int, input().split())
T = list(map(int, input().split()))

total_T = [0] * M

for _ in range(N):
    # 최소 대기시간의 놀이기구 찾기
    now_idx = get_min_idx(total_T)
    total_T[now_idx] += T[now_idx]

print(now_idx + 1)