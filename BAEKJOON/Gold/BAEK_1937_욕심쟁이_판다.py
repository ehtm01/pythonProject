# BAEK 1937. 욕심쟁이 판다
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
d = (-1, 0), (1, 0), (0, -1), (0, 1)

def panda(r, c):
    q = deque([(r, c)])
    if dp[r][c] == -1:
        dp[r][c] = 0
    while q:
        x, y = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if matrix[r][c] > matrix[ny][nx]:
                continue
            if dp[ny][nx] != -1:
                dp[ny][nx] = max(dp[ny][nx], dp[r][c] + 1)
            else:
                dp[ny][nx] = dp[r][c] + 1
                q.append((ny, nx))
    return max(best, dp[r][c] + 1)

best = 0
result = []
for i in range(n):
    for j in range(n):
        result.append(panda(i, j))

print(max(result))
