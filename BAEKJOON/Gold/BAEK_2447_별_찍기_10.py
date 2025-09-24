# BAEK 2447. 별 찍기 - 10
# 재귀, 분할정복 사용
import sys
sys.stdin = open('input.txt', 'r')
from math import log

N = int(input())
k = int(log(N, 3))
matrix = ['*' * N for _ in range(N)]

if k == 1:
