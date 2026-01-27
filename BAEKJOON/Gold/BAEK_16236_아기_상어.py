# BAEK 16236. 아기 상어
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline()

# 아기 상어보다 큰 물고기가 있는 칸은 지나갈 수 없음.
# 자신의 크기보다 작은 물고기만 먹을 수 있음.
# 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
# 처음 아기 상어의 크기는 2

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]