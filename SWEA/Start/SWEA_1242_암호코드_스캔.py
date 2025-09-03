# SWEA 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [int(input()) for _ in range(N)]