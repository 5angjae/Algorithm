# 분수 합
# 2/7 // 3/5
# 10+21/35

import math
# 최소공배수
# def lcm(a, b):
#     for i in range(max(a,b), (a*b)+1):
#         if i % a == 0 and i % b == 0:
#             return i

a, b = map(int, input().split())
c, d = map(int, input().split())

# answerd = lcm(ad, bd)
# answeru = au * (answerd // ad) + bu * (answerd // bd)
answerd = b * d
answeru = a * d + c * b
gcd = math.gcd(answeru, answerd)
answeru //= gcd
answerd //= gcd

print(answeru, answerd)