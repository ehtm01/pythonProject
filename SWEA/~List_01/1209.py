# 1209. [S/W 문제해결 기본] 2일차 - Sum
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AV13_BWKACUCFAYh&probBoxId=AZh9Dhq6vtHHBINp&type=PROBLEM&problemBoxTitle=0806_List2&problemBoxCnt=9

# import sys
# sys.stdin = open('input.txt', 'r')


for tc in range(1, 11):
    test_case = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    for i in range(100):
        sum_i = 0
        for j in range(100):
            sum_i += matrix[i][j]
        if sum_i > max_sum:
            max_sum = sum_i

    for j in range(100):
        sum_j = 0
        for i in range(100):
            sum_j += matrix[i][j]
        if sum_j > max_sum:
            max_sum = sum_j

    sum_x_1 = 0
    sum_x_2 = 0

    for i in range(100):
        sum_x_1 += matrix[i][i]
        if sum_x_1 > max_sum:
            max_sum = sum_x_1

        sum_x_2 += matrix[-i-1][i]
        if sum_x_2 > max_sum:
            max_sum = sum_x_2

    print(f'#{test_case} {max_sum}')