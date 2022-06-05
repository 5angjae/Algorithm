# BJ1561

> 이전 스터디 때 못풀었던 문제를 다시 풀어보았다.

### 다른 사람의 풀이

다른 사람의 풀이를 참고하여 방법을 이해하려고 했으나, 이분탐색을 하는 과정이 왜 저런 방식으로 이루어지는지 아직 이해하지 못했다.

```python
# BJ1561_놀이공원
# 20211123 / 20211221 두번 나온 문제
# 당시 힌트
# 1. 이분탐색을 통해서 아이들을 모두 태울 수 있는 시간을 찾는다.
# 2. 구한 시간 - 1분까지 몇명의 아이들을 태울 수 있는지 탐색한다.

N, M = map(int, input().split())
time_list = list(map(int, input().split()))
# N : 아이들 숫자
# M : 놀이기구 숫자

if N < M:
    print(N)
else:
    l, r = 0, 60000000000 # 최대 아이들 수 2000000000 * 최대 운행시간 30 으로 최대값
    t = None
    while l <= r:
        mid = (l+r)//2
        cnt = M
        for i in range(M):
            cnt += mid//time_list[i] ## 왜 이렇게 하는지 알아야 한다.
        if cnt >= N:
            t = mid
            right = mid - 1
        else:
            left = mid + 1

    for i in range(M):
        if t % time_list[i] == 0:
            cnt += 1
        if cnt == N:
            print(i+1)
            break
```

시간 초과가 나왔다. 이 문제는 아마 입력 방식에 따른 문제인 것 같다.

input() 과 sys.readline

의 차이인 것 같은데 조금 더 봐야 알 것 같다.



## sys.stdin.readline()을 활용했을 때

같은 코드에 입력 방식을 위로 바꿨을 때, 시간 초과가 안날줄 알았는데 여전히 났다.

분명 성공한 코드였을텐데 그냥 다시 처음부터 코드를 이해하고 짜봐야할 것 같다.