# BAEK 31246. 모바일 광고 입찰
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
K_lst = [0 for _ in range(N)]
for i in range(N):
    A, B = map(int, input().split())
    if A <= B:
        K_lst[i] = B - A

K_lst.sort()
print(K_lst[K - 1])