# 1216. [S/W 문제해결 기본] 3일차 - 회문2
import sys
sys.stdin = open('input.txt', 'r')

T = 10
N = 100


def longest_line(i):
    long = 1
    n = len(i)
    # 홀수 길이 중심: (j, j)
    for j in range(n):
        left = right = j
        while left >= 0 and right < n and i[left] == i[right]:
            long = max(long, right - left + 1)
            left -= 1
            right += 1
    # 짝수 길이 중심: (j, j+1)
    for j in range(n - 1):
        left, right = j, j + 1
        while left >= 0 and right < n and i[left] == i[right]:
            long = max(long, right - left + 1)
            left -= 1
            right += 1

    return long


for test_case in range(1, T+1):
    tc = int(input())
    matrix = [input() for _ in range(N)]
    matrix_trans = [''.join(col) for col in zip(*matrix)]

    result = 1
    for i in matrix:
        result = max(result, longest_line(i))

    for i in matrix_trans:
        result = max(result, longest_line(i))

    print(f'#{tc} {result}')
