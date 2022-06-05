def solution(clothes):
    clothes_dic = {}
    clothes_type = []
    for cloth in clothes:
        clothes_dic[cloth[1]] = []
        clothes_type.append(cloth[1])
    for cloth in clothes:
        clothes_dic[cloth[1]].append(cloth[0])
    c_type = set(clothes_type)
    total = 1
    for c in c_type:
        total *= (len(clothes_dic[c]) + 1)
    
    
    return total-1

# 맞는 풀이인지는 모르겠다 솔직히
# 타입 리스트를 추리고
# 타입 당, 의상 이름 리스트를 타입이름을 키값으로 dictionary에 넣고
# 각 키별로 길이를 확인해서 + 1씩 곱하고
# 1을 빼주면 된다.