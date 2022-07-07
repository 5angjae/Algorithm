# BOJ 2143 두 배열의 합
from itertools import combinations

def sum_dict(L):
    sum_L = []
    temp = 0
    result = {}
    sum_list = []
    for i in range(len(L)):
        temp += L[i]
        sum_L.append(temp)

    combi = list(combinations(range(len(L)), 2))
    # print(combi)

    for c in combi:
        if c[0] != 0:
            c_value = sum_L[c[1]]-sum_L[c[0]-1]
        else:
            c_value = sum_L[c[1]]

        if c_value not in result:
            result[c_value] = 1
            sum_list.append(c_value)
            # print(sum_list)
        else:
            result[c_value] += 1


    for i in range(len(L)):
        if L[i] not in result:
            result[L[i]] = 1
            sum_list.append(L[i])
        else:
            result[L[i]] += 1

    # print(result, sum_list)

    return [result, sum_list]

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sum_A = sum_dict(A)[0]
sum_B = sum_dict(B)[0]
A_sum_list = sum_dict(A)[1]
B_sum_list = sum_dict(B)[1]
A_sum_list.sort()
B_sum_list.sort()

# print(sum_A)
# print(A_sum_list)
# print(sum_B)
# print(B_sum_list)


i = 0
j = len(B_sum_list) - 1
cnt = 0
while i < len(A_sum_list) and j >= 0:

    temp = A_sum_list[i] + B_sum_list[j]
    # print(i, j, T, temp)
    if temp == T:
        cnt += (sum_A[A_sum_list[i]] * sum_B[B_sum_list[j]])
        if i != len(A_sum_list):
            i += 1
        else:
            j -= 1
    elif temp > T:
        j -= 1
    else:
        i += 1

print(cnt)



# A, B 각각에 대해 누적합 (중복 상관 X 1차원 배열에 넣고 정렬)
# A는 작은거부터 + 1 씩 idx / B는 큰거부터 -1 씩 idx 하면서 더하고 T랑 비교해서 크면 B 줄이고 작으면 A 올리고 T랑 같으면 cnt += 1
# 1 3 1 2
# 1 4 5 7
# 1 3 1 2