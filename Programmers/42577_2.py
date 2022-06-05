def solution(phone_book):
    answer = True
    phone_book.sort() # 정렬하면 똑같이 시작하는 것 끼리 붙어있게 된다.
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer

# 정렬을 너무 어렵게 하려고 했던게 문제인 것 같다.
