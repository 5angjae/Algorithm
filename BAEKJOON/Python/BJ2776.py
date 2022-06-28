# BJ2776_암기왕

def binary(s, e, nums, num):
    while s <= e:
        mid = (s+e)//2
        if num1[mid] == num:
            return 1
        elif num1[mid] < num:
            s = mid + 1
        else:
            e = mid - 1
    return 0
T = int(input())

for _ in range(T):
    N = int(input())
    num1 = list(map(int, input().split()))
    M = int(input())
    num2 = list(map(int, input().split()))
    
    num1.sort()

    for num in num2:
        if num < num1[0] or num > num1[N-1]:
            print(0)
        else:
            print(binary(0, N-1, num1, num))
