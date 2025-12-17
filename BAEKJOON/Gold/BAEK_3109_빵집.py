# BAEK 3109. 빵집
import sys
# from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 첫째 열은 근처 빵집의 가스관, 마지막 열은 원웅이의 빵집
# 건물이 있는 경우에는 파이프를 놓을 수 없다.
# 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 연결 가능
# 파이프라인의 경로는 겹칠 수 없고, 서로 접할 수도 없음 -> 각 칸을 지나는 파이프는 하나
# 파이프라인의 최댓값 구하기

R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

d = (-1, 1), (0, 1), (1, 1)
visited = [[False] * C for _ in range(R)]
# q = deque()

# for r in range(R):
#     q.append((r, 0))
#     visited[r][0] = True

#     while q:
#         y, x = q.popleft()
#         for dy, dx in d:
#             ny, nx = y + dy, x + dx
#             if ny < 0 or ny >= R or nx < 0 or nx >= C or visited[ny][nx] or grid[ny][nx] == 'x':
#                 continue
#             visited[ny][nx] = True
#             if nx == C - 1:
#                 break
#             q.append((ny, nx))


# DFS + Greedy
def pipeline(i, j):
    if j == C - 1:
        return True
    for di, dj in d:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= R or nj < 0 or nj >= C or visited[ni][nj] or grid[ni][nj] == 'x':
            continue
        visited[ni][nj] = True
        if pipeline(ni, nj):
            return True
    return False


cnt = 0
for r in range(R):
    visited[r][0] = True
    if pipeline(r, 0):
        cnt += 1

print(cnt)
