# BAEK 2138. 전구와 스위치
import sys
input = sys.stdin.readline

N = int(input())
current = list(map(int, input().strip()))
expect = list(map(int, input().strip()))

# print(current)
# print(expect)


# def dfs(array, idx, cnt):
#     global best
#     if array == expect:
#         best = min(best, cnt)
#         return
#     if idx >= N:
#         return
#     dfs(array, idx + 1, cnt)
#     for i in range(idx - 1, idx + 2):
#         if i < 0 or i >= N:
#             continue
#         if array[i]:
#             array[i] = 0
#         else:
#             array[i] = 1
#     dfs(array, idx + 1, cnt + 1)


# best = float('inf')
# dfs(current, 0, 0)
# print(best)