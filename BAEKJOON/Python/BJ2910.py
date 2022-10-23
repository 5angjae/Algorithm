# 빈도 정렬

N, C = map(int, input().split())
arr = list(map(int, input().split()))

arr_dict = {}
for a in arr:
    if a not in arr_dict:
        arr_dict[a] = 1
    else:
        arr_dict[a] += 1

sorted_dict = sorted(arr_dict.items(), key=lambda x:x[1], reverse=True)

answer = []
for sd in sorted_dict:
    for _ in range(sd[1]):
        answer.append(str(sd[0]))

print(" ".join(answer))