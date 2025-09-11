# SWEA 16977. 5일차 응용 - 전기버스2
import sys
sys.stdin = open("input.txt", "r")


def bus(idx):
    global min_exchange
    if idx == N:
        min_exchange = min(min_exchange, visited[idx])
        return

    for i in range(1, M[idx] + 1):
        if idx + i > N:
            continue
        if visited[idx + i] != -1 and visited[idx + i] < visited[idx] + 1:
            return
        else:
            visited[idx + i] = visited[idx] + 1
            bus(idx + i)


T = int(input())

for tc in range(1, T +1):
    M = list(map(int, input().split()))
    N = M[0]
    visited = [-1] * (N + 1)
    min_exchange = float('inf')

    bus(1)
    print(f'#{tc} {min_exchange}')
