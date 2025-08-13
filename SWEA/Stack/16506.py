# 16506. 4일차 - 그래프 경로
def find_node_DFS(s, N, G):
    visited = [0] * (N + 1)
    stack = []
    v = s

    visited[s] = 1
    while True:
        for nv in node_list[v]:
            if not visited[nv]:
                stack.append(v)
                v = nv
                visited[nv] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

    if visited[S] and visited[G]:
        return 1
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    node_list = [[] for _ in range(V + 1)]

    for i in range(E):
        s, e = map(int, input().split())
        node_list[s].append(e)

    S, G = map(int, input().split())

    print(f'#{tc} {find_node_DFS(S, V, G)}')
