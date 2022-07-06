# BOJ 20291 파일 정리
N = int(input())
files = [input() for _ in range(N)]
dict = {}

# d = {"a":234, "b":1 , "aaa": 123}
# if "a" not in d:
#     print("NO")
# else:
#     print(d["a"])
#
# for dic in d:
#     print(dic, d[dic])
for file in files:
    extension = ""
    exten_idx = 0
    for i in range(len(file)):
        if file[i] == ".":
            exten_idx = i
            break
    extension = file[exten_idx+1:]
    if extension not in dict:
        dict[extension] = 1
    else:
        dict[extension] += 1
result = []
for d in dict:
    result.append([d, dict[d]])

result.sort(key=lambda x:x[0])

for r in result:
    print(r[0], r[1])