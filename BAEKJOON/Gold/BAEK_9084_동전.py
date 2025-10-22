# BAEK 9084. 동전
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    dp = [0] * M
    for i in range(N):
        dp[arr[i]] = 1

    def solve(n):
        if n == M:
            return

        for j in range(N):
            a = arr[j]
            dp[n + a] = dp[n] + dp[a]