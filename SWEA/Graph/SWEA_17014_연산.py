# SWEA 17014. 6일차 응용 - 연산
import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    max_value = 1000000

    if N == M:
        print(f'#{tc} 0')
        continue

    visited = [0] * (max_value + 1)
    q = deque()
    q.append((N, 0))
    visited[N] = 1
    best = float('inf')

    while q:
        x, cnt = q.popleft()
        if x == M:
            best = min(best, cnt)
            break

        r = x + 1
        if r <= max_value and visited[r] == 0:
            visited[r] = 1
            q.append((r, cnt + 1))

        r = x - 1
        if r >= 1 and visited[r] == 0:
            visited[r] = 1
            q.append((r, cnt + 1))

        r = x * 2
        if r <= max_value and visited[r] == 0:
            visited[r] = 1
            q.append((r, cnt + 1))

        r = x - 10
        if r >= 1 and visited[r] == 0:
            visited[r] = 1
            q.append((r, cnt + 1))

    print(f'#{tc} {best}')
