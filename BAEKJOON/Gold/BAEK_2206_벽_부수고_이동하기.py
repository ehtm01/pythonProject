# BAEK 2206. 벽 부수고 이동하기
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
grid = [input() for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[0] for _ in range(N)]
