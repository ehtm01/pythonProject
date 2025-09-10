# SWEA 22310. 완벽한 정사각형
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    n = 1
    while n ** 2 < N:
        n += 1

    if n ** 2 == N:
        print(f'#{tc} {n}')
    else:
        print(f'#{tc} 0')
