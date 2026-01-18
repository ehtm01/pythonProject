# BAEK 24526. 전화 돌리기
# 노드
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 회장이 부원들에게 전화를 넘김
# 부원들도 다른 부원들에게 전화를 넘김
# 같은 부원이 두 번 전화받지 않게 하자.

N, M = map(int, input().split())
call = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    call[u].append(v)

call_cnt = 0
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    q = deque()
    if call[i]:
        for j in call[i]:
            q.append(j)
        while q:
            x = q.popleft()
            if visited[x]:
                break
            visited[x] = True
            for k in call[x]:
                q.append(k)
        else:
            call_cnt += 1
    else:
        call_cnt += 1

print(call_cnt)
