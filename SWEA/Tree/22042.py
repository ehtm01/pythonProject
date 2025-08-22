# 22042. 대칭 포화 이진 트리 판별하기
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))
    q = deque
    q.append(tree[0])
    visited = [0] * (N + 1)
    visited[tree[0]] = 1

    while q:
        x = q.popleft()
