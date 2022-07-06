# BOJ 1769 3의 배수
N = str(input())
cnt = 0
while len(N) > 1:
    temp = 0
    for i in range(len(N)):
        temp += int(N[i])
    cnt += 1
    N = str(temp)

print(cnt)
if int(N) % 3 == 0:
    print("YES")
else:
    print("NO")