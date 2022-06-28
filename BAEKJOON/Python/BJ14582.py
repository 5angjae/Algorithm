# BJ14582_오늘도졌다
# 첫줄 입력 : 울림 제미니스 득점
# 두번째줄 입력 : 스타트링크 걸리버스 득점
# 경기도중 이기고 있는 순간이 있으면 됨

Woollim = list(map(int, input().split()))
Startlink = list(map(int, input().split()))

winning_moment = 0
result = "No"


for i in range(9):
    winning_moment += Woollim[i]
    if winning_moment > 0:
        result = "Yes"
        break
    winning_moment -= Startlink[i]


print(result)