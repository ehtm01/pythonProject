# SWEA 10726. 이진수 표현
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} ON') if ((1 << N) - 1) & M == 2 ** N - 1 else print(f'#{tc} OFF')
