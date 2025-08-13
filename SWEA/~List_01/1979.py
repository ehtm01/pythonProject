# 1979. 어디에 단어가 들어갈 수 있을까
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AV5PuPq6AaQDFAUq&probBoxId=AZh9Dhq6vtHHBINp&type=PROBLEM&problemBoxTitle=0806_List2&problemBoxCnt=9

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        i_cnt = 0
        for j in range(N):
            if arr[i][j]:
                i_cnt += 1
            else:
                if i_cnt == K:
                    result += 1
                i_cnt = 0
        if i_cnt == K:
            result += 1

    for j in range(N):
        j_cnt = 0
        for i in range(N):
            if arr[i][j]:
                j_cnt += 1
            else:
                if j_cnt == K:
                    result += 1
                j_cnt = 0
        if j_cnt == K:
            result += 1

    print(f'#{test_case} {result}')
