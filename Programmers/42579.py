def solution(genres, plays):
    answer = []
    genres_plays = {}
    genres_set = set(genres)
    for genre in genres:
        genres_plays[genre] = [[],0]
    for i in range(len(genres)):
        genres_plays[genres[i]][1] += plays[i]
        genres_plays[genres[i]][0].append(i)
    
    sorted_dict = sorted(genres_plays.items(), key = lambda item: item[1][1], reverse=True)
    
    for genre in sorted_dict:
        genre[1][0].sort(key=lambda x:plays[x], reverse=True)
        if len(genre[1][0]) >= 2:
            answer.append(genre[1][0][0])
            answer.append(genre[1][0][1])
        elif len(genre[1][0]) == 1:
            answer.append(genre[1][0][0])
    return answer

# 아래 코드의 문제는 index 에러가 나면서 런타임에러가 났던 것이었다.
# 각 장르에 1개의 노래만 있을 때의 경우도 고려해준다면 위와 같이 코드를 추가하면 된다.

# def solution(genres, plays):
#     answer = []
#     genres_plays = {}
#     genres_set = set(genres)
#     for genre in genres:
#         genres_plays[genre] = [[],0]
#     for i in range(len(genres)):
#         genres_plays[genres[i]][1] += plays[i]
#         genres_plays[genres[i]][0].append(i)
    
#     sorted_dict = sorted(genres_plays.items(), key = lambda item: item[1][1], reverse=True)
    
#     for genre in sorted_dict:
#         genre[1][0].sort(key=lambda x:plays[x], reverse=True)
#         answer.append(genre[1][0][0])
#         answer.append(genre[1][0][1])
#     return answer

# 일부 테스트케이스에 대해서 런타임에러가 떴다.
# 코드 자체도 너무 복잡해서
# 좀 더 간단하게 할 방법을 찾아야겠다.