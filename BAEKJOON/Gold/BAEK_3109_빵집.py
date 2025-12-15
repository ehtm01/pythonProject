# BAEK 3109. 빵집
import sys
sys.stdin = open('input', 'r')
input = sys.stdin.readline

N = int(input())
for _ in range(N - 2):
    bridge = list(map(int, input().split()))
