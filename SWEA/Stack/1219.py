# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
def find_way(s, num):
    current = s
    visited = [0] * num
    stack = []
    visited[s] = 1

    while True:
        for new_current in way[current]:
            if not visited[new_current]:
                stack.append(current)
                current = new_current
                visited[new_current] = 1
                break
        else:
            if stack:
                current = stack.pop()
            else:
                break

    if visited[num - 1]:
        return 1
    return 0


T = 10

for t in range(1, T+1):
    N = 100
    tc, w = map(int, input().split())
    arr = list(map(int, input().split()))
    way = [[] for _ in range(N)]

    for i in range(w):
        start, end = arr[2 * i], arr[2 * i + 1]
        way[start].append(end)

    print(f'#{tc} {find_way(0, N)}')
