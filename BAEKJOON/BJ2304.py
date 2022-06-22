# BOJ2304 창고다각형 - 미완

# 지붕은 수평부분과 수직부분으로 구성 모두 연결
# 오목하게 들어간 부분 없는

def roof_left(pillars):
    pass


N = int(input())
pillars = [list(map(int, input().split())) for _ in range(N)]
# pillar = [L, H] // L : 위치 , H : 높이
# 제일 높은 거 뽑고
# 양쪽으로 가면서 다음 높은거로 사각형을 빼주는 방법?
pillars.sort()
max_pillar = []
max_height = 0
for pillar in pillars:
    if pillar[1] > max_height:
        max_pillar = pillar
        max_height = pillar[1]

print(max_pillar)