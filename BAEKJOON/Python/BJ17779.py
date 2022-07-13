# BOJ 17779 게리맨더링 2

# x, y, d1, d2 로 경계선 찾아서 5번 구역 찾고
# 5번 구역에 표시
# 각 구역별로 더하는데 표시된건 뺴고 더함

def min_dif(x,y,d1,d2):
    zone = [[0] * (N+1) for _ in range(N+1)]
    population = [0] * 6
    for i in range(d1+1):
        zone[x+i][y-i] = 5
        zone[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        zone[x+i][y+i] = 5
        zone[x+d1+i][y-d1+i] = 5
    # 여기까지 경계설정은 끝
    for i in range(x+1, x+d1+d2):# 경계사이의 공간을 채우기 (줄마다)
        state = False
        for j in range(1,N+1):
            if zone[i][j] == 5:
                state = not state
            if state:
                zone[i][j] = 5
    for r in range(1, N+1):
        for c in range(1, N+1):
            # 1번 선거구
            if r < x+d1 and c<= y and zone[r][c] == 0:
                #print(P[r][c])
                population[1] += P[r][c]
            # 2번 선거구
            elif r <= x+d2 and y<c and zone[r][c] == 0:
                population[2] += P[r][c]
            # 3번 선거구
            elif x+d1 <= r and c<y-d1+d2 and zone[r][c] == 0:
                population[3] += P[r][c]
            # 4번 선거구
            elif x+d2 < r and y-d1+d2 <= c and zone[r][c] == 0:
                population[4] += P[r][c]
            # 5번 선거구
            elif zone[r][c] == 5:
                population[5] += P[r][c]
    # for i in range(N+1):
    #     print(zone[i])
    #
    # print()
    return max(population[1:]) - min(population[1:])

N = int(input())
P = [[0]*(N+1)] + [([0] + list(map(int, input().split()))) for _ in range(N)]
#print(P)
result = 20*20*100
# 모든 x, y, d1, d2에 대해서??
# print(min_dif(2,3,1,2))
for x in range(1,N+1):
    for y in range(1,N+1):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                    # print(x, y, d1, d2, min_dif(x,y,d1,d2))
                    result = min(result, min_dif(x,y,d1,d2))

print(result)