# BAEK 14938. 서강그라운드
from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt', 'r')

n, m, r = map(int, input().split())
t = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    adj[a].append((l, b))
    adj[b].append((l, a))


def dijkstra(s):
    pq = [(0, s)]
    best = [float('inf')] * (n + 1)
    best[s] = 0

    while pq:
        dist, node = heappop(pq)
        if dist > m or best[node] < dist:
            continue

        for n_dist, n_node in adj[node]:
            n_dist = dist + n_dist

            if n_dist > m or best[n_node] <= n_dist:
                continue

            best[n_node] = n_dist
            heappush(pq, (n_dist, n_node))
    return best


ans = 0
for i in range(1, n + 1):
    arr = dijkstra(i)
    item = 0
    for j in range(1, n + 1):
        if arr[j] != float('inf'):
            item += t[j - 1]
    ans = max(item, ans)

print(ans)
