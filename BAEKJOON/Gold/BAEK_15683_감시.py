# BAEK 15683. 감시
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

d = {1: [(0, 1), (1, 0), (0, -1), (-1, 0)],
     2: []}