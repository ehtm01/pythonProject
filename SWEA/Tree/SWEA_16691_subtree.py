# 16691. 8일차 - subtree
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    num_cou = list(map(int, input().split()))
    visited = [0] * (E + 2)
    adj_l = [[] for _ in range(E + 2)]

    for i in range(E):
        s, e = num_cou[2 * i], num_cou[2 * i + 1]
        adj_l[s].append(e)

    q = deque()
    q.append(N)
    visited[N] = 1

    while q:
        x = q.popleft()
        for t in adj_l[x]:
            if not visited[t]:
                visited[t] = 1
                q.append(t)

    print(f'#{tc} {sum(visited)}')
