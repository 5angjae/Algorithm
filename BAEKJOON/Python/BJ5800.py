K = int(input())
# grades = [list(map(int, input().split())) for _ in range(K)]
for c in range(1, K+1):
    grades = list(map(int, input().split()))[1:]
    grades.sort(reverse=True)
    print("Class", c)
    lgap = 0
    for i in range(len(grades)-1):
        if lgap < grades[i] - grades[i+1]:
            lgap = grades[i] - grades[i+1]
    #print("Max", grades[0], ", Min", grades[-1], ", Largest gap", lgap)
    print(f"Max {grades[0]}, Min {grades[-1]}, Largest gap {lgap}")