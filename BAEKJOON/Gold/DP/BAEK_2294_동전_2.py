# BAEK 2294. 동전 2
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

# dp 배열 초기화
# -1은 해당 금액을 만들 수 없음을 의미
dp = [-1] * (k+1)
# 0원을 만드는 방법은 0개이므로 0으로 초기화
dp[0] = 0

# 각 동전을 순회하며 동전의 크기만큼 넘어가며 더해줌
for c in coin:
    # 동전의 크기만큼 넘어가며 더해줌
    for i in range(c, k+1):
        if dp[i] == -1:
            if dp[i-c] != -1:
                dp[i] = dp[i-c] + 1
        else:
            if dp[i-c] != -1:
                dp[i] = min(dp[i], dp[i-c] + 1)
        
print(dp[k])
