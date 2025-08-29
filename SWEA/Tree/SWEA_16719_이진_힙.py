# SWEA 16719. 8일차 - 이진 힙
T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())
    arr = list(map(int, input().split()))
    heap = [0] * (N + 1)
    last = 0

    for n in arr:
        last += 1
        heap[last] = n

        c = last
        p = c // 2

        while p and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = c // 2

    sum = 0
    while last > 1:
        last //= 2
        sum += heap[last]

    print(f'#{tc} {sum}')
