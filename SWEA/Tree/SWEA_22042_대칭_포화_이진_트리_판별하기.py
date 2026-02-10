# 22042. 대칭 포화 이진 트리 판별하기
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))
    q = deque()
    n = 1
    ok = True
    for i in range(N):
        q.append(tree[i])

    if q.popleft() == 1:
        while q:
            left = []
            right = []
            for i in range(n):
                left.append(q.popleft())
            for j in range(n):
                right.append(q.popleft())
            if left != right[::-1]:
                ok = False
                break
            n *= 2
    else:
        ok = False

    print(f'#{tc} {ok}')
