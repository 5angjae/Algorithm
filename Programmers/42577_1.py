def solution(phone_book):
    phone_book.sort(key=lambda x:len(x))
    
    cnt = 0
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                cnt += 1
                
                
    if cnt == 0:
        return True
    else:
        return False

# 이 코드는 이중 for 문을 활용해서 찾는 방식을 사용했다.
# 정확하게 다 찾긴 했지만, 시간초과가 나서 새로운 방식을 시도해봐야 한다.