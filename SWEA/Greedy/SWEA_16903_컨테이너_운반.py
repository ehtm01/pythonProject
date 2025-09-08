# SWEA 16903. 3일차 응용 - 컨테이너 운반
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    sum_weight = 0
    weight.sort(reverse=True)
    truck.sort(reverse=True)

    for w in weight:
        if truck:
            if w > truck[0]:
                continue
            else:
                sum_weight += w
                truck[0] = 0
                truck.sort(reverse=True)

    print(f'#{tc} {sum_weight}')
