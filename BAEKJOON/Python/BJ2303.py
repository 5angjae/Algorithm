# BOJ 2303 숫자 게임
import itertools

N = int(input())
max_person = 0
max_number = 0
for i in range(N):
    cards = list(map(int, input().split()))
    three_cards = itertools.combinations(cards, 3)
    max_cards = 0
    for three_card in three_cards:
        if max_cards < (sum(three_card)%10):
            max_cards = (sum(three_card)%10)
    #print(max_cards)
    if max_number <= max_cards:
        max_number = max_cards
        max_person = i

print(max_person + 1)