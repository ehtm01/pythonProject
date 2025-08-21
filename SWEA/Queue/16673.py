# 16673. 6일차 - 노드의 거리
from collections import deque

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    node_num = [list(map(int, input().split())) for _ in range(E)]
    arr = []

    for i in node_num:
        arr.extend(i)

    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    q = deque()

    adj_l = [[] for _ in range(V + 1)]
    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)

    def find_path(s, v):
        q.append(s)

        while q:
            t = q.popleft()
            if t == v:
                return visited[t] + 1
            for w in adj_l[t]:
                if not visited[w]:
                    q.append(w)
                    visited[w] = visited[t] + 1

    find_path(S, G)
    print(f'#{tc} {visited[G]}')
