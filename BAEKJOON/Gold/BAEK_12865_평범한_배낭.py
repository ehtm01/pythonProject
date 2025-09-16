# BAEK 12865. 평범한 배낭
import sys
sys.stdin = open('input.txt', 'r')


def backpack(idx, w, v):
    if w > K:
        return v
    dp[idx] += backpack(idx, w + arr[idx][0], v + arr[idx][1])

N, K = map(int, input().split())
arr = []
for _ in range(N):
    W, V = map(int, input().split())
    arr.append((W, V))

arr.sort()
dp = [0] * N
best = 0
backpack(0)