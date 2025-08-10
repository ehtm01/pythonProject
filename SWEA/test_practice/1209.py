# 1209. [S/W 문제해결 기본] 2일차 - Sum

T = 10

import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, T + 1):
    input()
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    x_sum_1 = 0
    x_sum_2 = 0

    for i in range(N):
        i_sum = 0
        j_sum = 0
        x_sum_1 += matrix[i][i]
        x_sum_2 += matrix[-i][i]
        for j in range(N):
            i_sum += matrix[i][j]
            j_sum += matrix[j][i]

        max_sum = max(max_sum, i_sum, j_sum, x_sum_1, x_sum_2)

    print(f'#{test_case} {max_sum}')
