# 1974. 스도쿠 검증
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AV5Psz16AYEDFAUq&probBoxId=AZh9Dhq6vtHHBINp&type=PROBLEM&problemBoxTitle=0806_List2&problemBoxCnt=9

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    result = 1
    matrix = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        if len(set(matrix[i])) != 9:
            result = 0

    if result:
        for j in range(9):
            arr = []
            for i in range(9):
                arr.append(matrix[i][j])
            if len(set(arr)) != 9:
                result = 0

    if result:
        for a in range(3):
            for b in range(3):
                matrix_9 = []
                for i in range(a*3, a*3+3):
                    for j in range(b*3, b*3+3):
                        matrix_9.append(matrix[i][j])
                if len(set(matrix_9)) != 9:
                    result = 0

    print(f'#{test_case} {result}')
