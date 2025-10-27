# BAEK 17298. 오큰수
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))

stack = []
ans = [0] * N
for i in range(N):
    if not stack:
        stack.append(i)
    else:
        if A[stack[-1]] < A[i]:
            while stack and A[stack[-1]] < A[i]:
                ans[stack[-1]] = A[i]
                stack.pop()
            stack.append(i)
        else:
            stack.append(i)

if stack:
    for k in range(len(stack)):
        ans[stack[k]] = -1
    stack = []

print(*ans)