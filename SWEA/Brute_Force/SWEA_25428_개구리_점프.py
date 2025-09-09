# SWEA 25428. 개구리 점프
import sys
sys.stdin = open("input.txt", "r")


def jump(idx):
    global max_dist

    for i in range(1, K + 1):
        if idx + i <= N - 1:
            if arr[idx + i]:
                jump(idx + i)
        else:
            max_dist = N
            break
    else:
        max_dist = max(max_dist, idx + K + 1)
        return

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    max_dist = 0
    jump(0)

    print(f'#{tc} {max_dist}')
