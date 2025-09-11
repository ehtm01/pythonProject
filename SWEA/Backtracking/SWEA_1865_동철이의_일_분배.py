# SWEA 1865. 동철이의 일 분배
import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    best = 0
    work = [-1] * N


    def company(idx, percent):
        global best
        if percent < best:
            return

        if idx == N:
            best = max(best, percent)
            return

        for i in range(N):
            if work[i] != -1:
                continue
            if matrix[idx][i] == 0:
                continue
            work[i] = idx
            x = matrix[idx][i] / 100
            company(idx + 1, percent * x)
            work[i] = -1


    company(0, 100)
    print(f'#{tc}{best: .6f}')
