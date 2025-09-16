# SWEA 17029. 7일차 응용 - 최소 비용
import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop, heappush

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
