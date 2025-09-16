# SWEA 17028. 7일차 응용 - 최소 신장 트리
import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop, heappush

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # # 1) 인접 리스트 + prim
    # edge = [[] for _ in range(V + 1)]
    # for _ in range(E):
    #     s, e, w = map(int, input().split())
    #     edge[s].append((e, w))
    #     edge[e].append((s, w))
    #
    # pq = [(0, 0)]
    # MST = [0] * (V + 1)
    # min_w = 0
    # curr_v = 0
    #
    # while curr_v < V + 1 and pq:
    #     weight, node = heappop(pq)
    #
    #     if MST[node]:
    #         continue
    #
    #     MST[node] = 1
    #     min_w += weight
    #     curr_v += 1
    #
    #     for nv, nw in edge[node]:
    #         if MST[nv]:
    #             continue
    #         heappush(pq, (nw, nv))
    #
    # print(f'#{tc} {min_w}')

    # 2) 인접 행렬 + Kruskal
    edges = []

    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))

    edges.sort(key=lambda x: x[2])

    p = [i for i in range(V + 1)]

    def find_set(x):
        if p[x] == x:
            return x

        p[x] = find_set(p[x])
        return p[x]

    def union(x, y):
        rep_x, rep_y = find_set(x), find_set(y)

        if rep_x == rep_y:
            return

        p[rep_y] = rep_x


    sum_e = 0
    min_w = 0

    for s, e, w in edges:
        if find_set(s) != find_set(e):
            union(s, e)
            sum_e += 1
            min_w += w
            if sum_e == V:
                break

    print(f'#{tc} {min_w}')
