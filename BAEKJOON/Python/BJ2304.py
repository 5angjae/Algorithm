# BOJ2304 창고다각형 - 미완

# 지붕은 수평부분과 수직부분으로 구성 모두 연결
# 오목하게 들어간 부분 없는

def roof_left(pillars, max_p):
    global size
    #print(size)
    left_pillars = []

    for pillar in pillars:
        if pillar[0] < max_p[0]:
            left_pillars.append(pillar)

    if len(left_pillars) == 0:
        return 0

    max_left_p = []
    max_left_height = 0
    min_left_position = 1001
    for p in left_pillars:
        if p[1] > max_left_height:
            max_left_p = p
            max_left_height = p[1]
        if p[0] < min_left_position:
            min_left_position = p[0]
    #print(max_p[1], max_left_height, max_p[0], min_left_position)
    size -= (max_p[1] - max_left_height) * (max_p[0] - min_left_position)

    roof_left(left_pillars, max_left_p)

def roof_right(pillars, max_p):
    global size
    #print(size)
    right_pillars = []

    for pillar in pillars:
        if pillar[0] > max_p[0]:
            right_pillars.append(pillar)

    if len(right_pillars) == 0:
        return 0

    max_right_p = []
    max_right_height = 0
    max_right_position = 0
    for p in right_pillars:
        if p[1] > max_right_height:
            max_right_p = p
            max_right_height = p[1]
        if p[0] > max_right_position:
            max_right_position = p[0]
    #print(max_p[1], max_right_height, max_p[0], max_right_position)
    size -= (max_p[1] - max_right_height) * (max_right_position - max_p[0])

    roof_right(right_pillars, max_right_p)

N = int(input())
pillars = [list(map(int, input().split())) for _ in range(N)]
# pillar = [L, H] // L : 위치 , H : 높이
# 제일 높은 거 뽑고
# 양쪽으로 가면서 다음 높은거로 사각형을 빼주는 방법?
pillars.sort()
max_pillar = []
max_height = 0
max_position = 0
min_position = 1001
for pillar in pillars:
    if pillar[1] > max_height:
        max_pillar = pillar
        max_height = pillar[1]
    if pillar[0] > max_position:
        max_position = pillar[0]
    if pillar[0] < min_position:
        min_position = pillar[0]

size = max_height * (max_position - min_position + 1)
roof_left(pillars, max_pillar)
roof_right(pillars, max_pillar)
print(size)