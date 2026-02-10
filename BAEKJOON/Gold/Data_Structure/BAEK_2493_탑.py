# BAEK 2493. 탑
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))

stack = []  # (탑의 인덱스, 탑의 높이)
result = []

for i in range(N):
    # 현재 탑보다 낮은 탑은 모두 제거
    while stack and stack[-1][1] < tower[i]:
        stack.pop()
    # 스택이 비었다면 왼쪽에 나보다 높은 탑이 없으므로 0
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0] + 1)  # 인덱스는 1-based
    stack.append((i, tower[i]))

print(' '.join(map(str, result)))