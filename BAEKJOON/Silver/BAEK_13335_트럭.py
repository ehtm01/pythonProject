# BAEK 13335. 트럭
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# n 개의 트럭, 다리 위에는 w 개의 트럭이 동시에 올라갈 수 있음(다리의 길이: w)
# 트럭들은 하나의 단위 시간에 하나의 단위 길이만큼 이동
# 다리가 견딜 수 있는 최대 하중은 L

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
t = 0
weight = 0

for i in range(n):
    if w == 1:
        t += 1
    else:
        weight += trucks[i]
        if weight > L:
            t += w - 1
        t += 1

print(t + w)
