# 1868. 파핑파핑 지뢰찾기
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mine = [input() for _ in range(N)]

    def minesweeper():
