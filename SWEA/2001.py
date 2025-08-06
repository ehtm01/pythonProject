# 2001. 파리 퇴치
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AV5PzOCKAigDFAUq&probBoxId=AZh9Dhq6vtHHBINp&type=PROBLEM&problemBoxTitle=0806_List2&problemBoxCnt=9

# import sys

# sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        fly = list(map(int, input().split()))
        for j in range(N):
            arr[i][j] = fly[j]

    max_sum = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_fly = 0
            for k in range(i, i + M):
                for a in range(j, j + M):
                    sum_fly += arr[k][a]

            if max_sum < sum_fly:
                max_sum = sum_fly

    print(f'#{test_case} {max_sum}')
