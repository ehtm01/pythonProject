# SWEA 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(range(1, 13))
    cnt = 0

    def subset(idx, arr):
        global cnt
        if len(arr) == N and sum(arr) == K:
            cnt += 1
            return

        if idx == 12:
            return

        subset(idx + 1, arr + [numbers[idx]])
        subset(idx + 1, arr)

    subset(0, [])
    print(f'#{tc} {cnt}')
