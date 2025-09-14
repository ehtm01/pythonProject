# SWEA 5650. [모의 SW 역량테스트] 핀볼 게임
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
block = [
     0, {0: 2, 1: 3, 2: 1, 3: 0},
        {0: 1, 1: 3, 2: 0, 3: 2},
        {0: 3, 1: 2, 2: 0, 3: 1},
        {0: 2, 1: 0, 2: 3, 3: 1},
        {0: 2, 1: 3, 2: 0, 3: 1}
         ]

dy = (-1, 0, 1, 0)
dx = (0, 1, 0 ,-1)


def best(score):
    global best_score
    best_score = max(best_score, score)


def play(row, col, direction):
    global recur, best_score
    cnt = 0
    sr, sc = row, col

    while True:
        row += dy[direction]
        col += dx[direction]
        # N x N 넘어서서 벽 맞았을 때
        if row < 0 or row >= N or col < 0 or col >= N:
            best(cnt * 2 + 1)
            return
        else:
            # 블랙홀 들어가면 끝
            if matrix[row][col] == -1 or (sr, sc) == (row, col):
                best(cnt)
                return
            # 도형 맞았을 때
            elif matrix[row][col] in range(1, 6):
                if block[matrix[row][col]][direction] == (direction + 2) % 4:
                    best(cnt * 2 + 1)
                    return
                next_d = block[matrix[row][col]][direction]
                direction = next_d
                cnt += 1
            # 웜홀 만났을 때
            elif matrix[row][col] in range(6, 11):
                w_num = matrix[row][col] - 6
                if (row, col) == wormhole[w_num][0]:
                    row = wormhole[w_num][1][0]
                    col = wormhole[w_num][1][1]
                else:
                    row = wormhole[w_num][0][0]
                    col = wormhole[w_num][0][1]


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 정사각형 + 4가지 형태 삼각형 블록 + 웜홀, 블랙홀
    # 블록이나 벽을 맞으면 진행방향 꺾이거나 반대
    # 웜홀은 쌍으로 주어지며 진행방향 동일
    # 핀볼이 출발 위치로 돌아오거나 블랙홀 만나면 게임 종료
    # 벽이나 블록에 부딪힌 횟수 = 점수
    # 출발 위치와 진행 방향 임의로 선정 가능
    # 점수 최댓값 구하기

    # 웜홀 쌍 만들기
    wormhole = [[] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] in range(6, 11):
                wormhole[matrix[i][j] - 6].append((i, j))

    best_score = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                comeback = (i, j)
                for d in range(4):
                    play(i, j, d)

    print(f'#{tc} {best_score}')
