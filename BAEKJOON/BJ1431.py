def num_sum(text):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    total = 0
    for t in text:
        if t in numbers:
            total += int(t)
    return total

N = int(input())

# serial / len / num_sum / sort
serials = []
for _ in range(N):
    s = input()
    serials.append(s)

serials.sort(key = lambda x:(len(x), num_sum(x), x))

for s in serials:
    print(s)