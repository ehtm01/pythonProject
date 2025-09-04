# SWEA 16886. 2일차 응용 - 전자카트
import sys
sys.stdin = open("input.txt", "r")

def solve(n):
    global min_sum

    if min_sum < sum(path):
        return

    if n == N:
        if min_sum:
            min_sum = min(min_sum, sum(path))
        else:
            min_sum = sum(path)

    for i in range(1, N):
        if visited[]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split()))]
    path = []
    min_sum = 0
    visited = [False] * N