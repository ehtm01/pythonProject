# SWEA 16720. 8일차 - 노드의 합
def postorder(t):
    if t <= N // 2:
        postorder(t * 2)
        postorder(t * 2 + 1)
        if t * 2 + 1 <= N:
            tree[t] = tree[t * 2] + tree[t * 2 + 1]
        else:
            tree[t] = tree[t * 2]

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for i in range(M):
        leap, num = map(int, input().split())
        tree[leap] = num

    postorder(L)
    print(f'#{tc} {tree[L]}')
