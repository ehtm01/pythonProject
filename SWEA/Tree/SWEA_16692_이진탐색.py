# 16692. 8일차 - 이진탐색
from collections import deque

def inorder(t):

    if t <= N:
        inorder(t * 2)
        tree[t] = q.popleft()
        inorder(t * 2 + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    q = deque()
    for i in range(1, N + 1):
        q.append(i)

    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')
