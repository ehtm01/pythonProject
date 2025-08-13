# 12712. 파리퇴치3
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AXuARWAqDkQDFARa&probBoxId=AZh9Dhq6vtHHBINp&type=USER&problemBoxTitle=0806_List2&problemBoxCnt=9

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        fly = list(map(int, input().split()))
        for j in range(N):
            arr[i][j] = fly[j]

    max_sum = 0

    plus_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(N):
        for j in range(N):
            sum_plus = sum_x = arr[i][j]
            for di, dj in plus_dirs:
                for dist in range(1, M):
                    ni, nj = i + di * dist, j + dj * dist
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_plus += arr[ni][nj]
            for di, dj in x_dirs:
                for dist in range(1, M):
                    ni, nj = i + di * dist, j + dj * dist
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_x += arr[ni][nj]

            max_sum = max(max_sum, max(sum_plus, sum_x))

    print(f'#{test_case} {max_sum}')
