# BAEK 17352. 여러분의 다리가 되어 드리겠습니다!
import sys
sys.stdin = open('input', 'r')
input = sys.stdin.readline

N = int(input())
for _ in range(N - 2):
    bridge = list(map(int, input().split()))
