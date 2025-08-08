# 1221. [S/W 문제해결 기본] 5일차 - GNS
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AV14jJh6ACYCFAYD&probBoxId=AZiHADjae2zHBINp&type=PROBLEM&problemBoxTitle=0808_String&problemBoxCnt=3

import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # test_count, N = map(str, input().split())
    # num = list(map(str, input().split()))
    # size_compare = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    #
    # for i in range(int(N)-1, 0, -1):
    #     for j in range(i):
    #         if size_compare.index(num[j]) > size_compare.index(num[j+1]):
    #             num[j], num[j+1] = num[j+1], num[j]
    test_count, N = map(str, input().split())
    N = int(N)
    num = list(map(str, input().split()))
    cnt = [0] * 10
    size_compare = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    results = [None] * N

    for i in num:
        cnt[size_compare.index(i)] += 1

    for i in range(1, 10):
        cnt[i] += cnt[i-1]

    for i in range(N-1, -1, -1):
        cnt[size_compare.index(num[i])] -= 1
        results[cnt[size_compare.index(num[i])]] = num[i]

    result = ' '.join(map(str, results))

    print(f'{test_count} {result}')
