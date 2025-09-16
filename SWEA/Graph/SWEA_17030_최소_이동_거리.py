# SWEA 17030. 7일차 응용 - 최소 이동 거리
import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop, heappush

T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(E)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))
    INF = float('inf')
    D = [INF] * (N + 1)

    pq = [(0, 0)]
    D[0] = 0

    while pq:
        weight, node = heappop(pq)
        if weight > D[node]:
            continue
        for nv, nw in adj[node]:
            nd = weight + nw
            if nd < D[nv]:
                D[nv] = nd
                heappush(pq, (nd, nv))

    print(f'#{tc} {D[N]}')
