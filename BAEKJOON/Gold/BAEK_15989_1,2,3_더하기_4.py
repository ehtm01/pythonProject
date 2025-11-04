# BAEK 15989. 1, 2, 3 더하기 4
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    n = int(input())
    # dp?
    dp = [0] * n
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3