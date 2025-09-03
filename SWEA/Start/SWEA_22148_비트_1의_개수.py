# SWEA 22148. 비트 1의 개수
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    remain = ''
    cnt = 0

    while N > 0:
        remain = str(N % 2) + remain
        if N % 2 == 1:
            cnt += 1
        N //= 2

    print(f'#{tc} {cnt}')
