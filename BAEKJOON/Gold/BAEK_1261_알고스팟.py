# BAEK 1261. 알고스팟
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 미로는 N * M 크기, 총 1 * 1 크기의 방으로 이뤄져 있음
# 상하좌우로 인접한 빈 방으로 이동할 수 있음
# 벽은 부술 수 있음
# (1, 1) -> (N, M) 이동하는데 부숴야 하는 벽의 최솟값 구하기

M, N = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]

# dp 사용
dp = [[float('inf')] * M for _ in range(N)]
dp[0][0] = 0
q = deque([(0, 0)])     # 덱 사용
d = (0, 1), (1, 0), (0, -1), (-1, 0)

while q:
    y, x = q.popleft()
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        # # 일반적인 BFS
        # if dp[ny][nx] != -1 and dp[ny][nx] <= dp[y][x]:
        #     continue
        # if maze[ny][nx] == '1':
        #     q.append((ny, nx))
        #     dp[ny][nx] = dp[y][x] + 1
        # else:
        #     q.appendleft((ny, nx))
        #     dp[ny][nx] = dp[y][x]
        # # 0-1 BFS
        # 다음으로 이동할 칸의 벽 유무 여부에 따른 벽 파괴 변수 생성
        next_cnt = dp[y][x] + (1 if maze[ny][nx] == '1' else 0)
        # 다음 칸의 dp 값이 더 크면 바꾼다.
        if next_cnt < dp[ny][nx]:
            dp[ny][nx] = next_cnt
            # 벽이면 deque의 오른쪽, 빈 방이면 deque의 왼쪽에 넣는다.
            if maze[ny][nx] == '1':
                q.append((ny, nx))
            else:
                q.appendleft((ny, nx))

print(dp[N-1][M-1])
