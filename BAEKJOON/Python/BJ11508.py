# BOJ11508 2+1 세일

N = int(input())
prices = [int(input()) for _ in range(N)]

prices.sort(reverse=True)

total = 0
for i in range(N):
    if i % 3 == 2:
        pass
    else:
        total += prices[i]

print(total)