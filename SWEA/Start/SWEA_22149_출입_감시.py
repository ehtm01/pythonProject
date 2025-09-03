# SWEA 22149. 출입 감시
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    people = list(map(int, input().split()))

    remain_id = [0] * 20001
    for p in people:
        if not remain_id[p]:
            remain_id[p] = 1
        else:
            remain_id[p] ^= 1
    print(remain_id.index(1))

    result = remain_id.index(1)

    if remain_id.index(1) > 10000:
        result -= 20001

    print(f'#{tc} {result}')
