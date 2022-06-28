def recursive(k):
    if k == 0:
        return pattern
    else:
        result = [' '] * (2**k)
    recursive(k-1)
# 0 5 * 5
# 1 11 * 11
# 2 23 * 23
# 원래 길이 // 2 + 1 을 빈칸 채우고 recursive(k-1) 채우고 나머지도 빈칸
# 다음 줄에 recursive(k-1) 채우고 1칸씩 빈칸 채우고 recursive(k-1)

    result = []

N = int(input())
N //= 3
k = 0
while N != 1:
    N //= 2
    k += 1

pattern = [[' ',' ','*',' ',' '],[' ','*',' ','*',' '],['*','*','*','*','*']]

if k == 0:
    result = pattern
else:
    pass # 나중에 다시 풀 예정