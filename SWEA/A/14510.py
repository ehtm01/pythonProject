# 14510. 나무 높이
import sys
sys.stdin = open('input.txt.', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))
    day = 0
    odd = []
    even = []

    for n in H:
        diff = max(H) - n
        if diff % 2 == 1:
            odd.append(1)
            if diff != 1:
                even.append(diff - 1)
        elif diff != 0:
            even.append(diff)

    while odd:
        even.sort()
        if even:
            even[-1] -= 2
            if not even[-1]:
                even.pop()
            day += 1
        else:
            break
        odd.pop()
        day += 1

    if odd:
        day += len(odd) * 2 - 1

    if even:
        k = sum(even) % 3
        day += (sum(even) // 3) * 2 + k

    print(f'#{tc} {day}')
