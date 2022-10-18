N, M = map(int, input().split())
P = []
for _ in range(M):
    P.append(int(input()))

P.sort()

max_total = 0
max_price = 0
for i in range(M):
    if M-i <= N:
        price = P[i] * (M-i)
    else:
        price = P[i] * N
    if max_total < price:
        max_total = price
        max_price = P[i]

print(max_price, max_total)
