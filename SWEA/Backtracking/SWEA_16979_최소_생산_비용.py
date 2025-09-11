# SWEA 16979. 5일차 응용 - 최소 생산 비용
import sys
sys.stdin = open("input.txt", "r")


def factory(idx, s):
    global min_sum
    if s >= min_sum:
        return
    if idx == N:
        min_sum = min(min_sum, s)
    for j in range(N):
        if visited[j]:
            continue
        visited[j] = 1
        factory(idx + 1, s + matrix[idx][j])
        visited[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    visited = [0] * N

    factory(0, 0)
    print(f'#{tc} {min_sum}')
