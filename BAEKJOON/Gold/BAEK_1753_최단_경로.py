# BAEK 1753. 최단 경로
from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
K = int(input())

adj = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))


def dijkstra(s):
    pq = [(0, s)]
    best = [float('inf')] * (V + 1)
    best[s] = 0

    while pq:
        dist, n = heappop(pq)

        if best[n] < dist:
            continue

        for n_dist, n_n in adj[n]:
            n_dist = dist + n_dist

            if best[n_n] <= n_dist:
                continue

            best[n_n] = n_dist
            heappush(pq, (n_dist, n_n))
    return best


arr = dijkstra(K)

for i in range(1, V + 1):
    if arr[i] != float('inf'):
        print(arr[i])
    else:
        print('INF')
