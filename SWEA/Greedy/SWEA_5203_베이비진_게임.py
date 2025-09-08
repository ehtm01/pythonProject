# SWEA 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    card_count_1 = [0] * 10
    card_count_2 = [0] * 10
    card = list(map(int, input().split()))
    winner = 0

    for i in range(12):
        if i % 2 == 0:
            card_count_1[card[i]] += 1
        else:
            card_count_2[card[i]] += 1

        if i >= 5:
            if card_count_1[card[i]] >= 3 or card_count_2[card[i]] >= 3:
                winner = i % 2 + 1
                break

            for n in range(8):
                if ((card_count_1[n] > 0 and card_count_1[n + 1] > 0 and card_count_1[n + 2] > 0) or
                        (card_count_2[n] > 0 and card_count_2[n + 1] > 0 and card_count_2[n + 2] > 0)):
                    winner = i % 2 + 1
                    break
        if winner:
            break

    print(f'#{tc} {winner}')
