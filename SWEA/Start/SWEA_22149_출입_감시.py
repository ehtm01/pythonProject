# SWEA 22149. 출입 감시
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    people = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            if people[i] == people[j]:
                people[i] = people[j] = 10001

    result = []

    for i in people:
        if i != 10001:
            result.append(i)

    print(f'#{tc} {"".join(map(str, result))}')
