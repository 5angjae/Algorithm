# BOJ 9625 BABBA


K = int(input())

result = [[0, 0] for _ in range(K+1)]
result[0] = [1, 0]

# result[i] = [a, b]
# result[i+1] = [b , a+b]

for i in range(1, K+1):
    result[i] = [result[i-1][1], result[i-1][0]+result[i-1][1]]

print(result[K][0], result[K][1])