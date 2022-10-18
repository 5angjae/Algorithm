N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

JperL = {}
for i in range(N):
    if L[i] == 0:
        JperL[i] = 101
    else:
        JperL[i] = J[i]/L[i]

sorted_dict = sorted(JperL.items(), key = lambda item: (-item[1], L[item[0]]))


total = 0
answer = 0
for sorted_value in sorted_dict:
    total += L[sorted_value[0]]
    if total >= 100:
        break
    else:
        answer += J[sorted_value[0]]

print(answer)