# 1873. 상호의 배틀필드
def battle_field(forward, row, col, n):
    if n == len(actions):
        return

    action = actions[n]
    forward_i = direction.index(forward)

    if action == 'S':
        di, dj = row + D[forward_i][0], col + D[forward_i][1]
        while 0 <= di < H and 0 <= dj < W:
            area = game_map[di][dj]
            if area == '*':
                game_map[di][dj] = '.'
                break
            if area == '#':
                break
            di, dj = di + D[forward_i][0], dj + D[forward_i][1]
        battle_field(forward, row, col, n + 1)
        return

    actions_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    i = actions_dict[action]
    game_map[row][col] = direction[i]
    ni, nj = row + D[i][0], col + D[i][1]
    if 0 <= ni < H and 0 <= nj < W and game_map[ni][nj] == '.':
        game_map[ni][nj] = direction[i]
        game_map[row][col] = '.'
        row, col = ni, nj

    battle_field(direction[i], row, col, n + 1)


T = int(input())

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    game_map = [list(input().strip()) for _ in range(H)]
    N = int(input())
    actions = input().strip()

    direction = ['^', 'v', '<', '>']
    D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    tank, row_tank, col_tank = '', 0, 0

    for r in range(H):
        for c in range(W):
            if game_map[r][c] in direction:
                tank = game_map[r][c]
                row_tank, col_tank = r, c
                break
        if tank:
            break

    battle_field(tank, row_tank, col_tank, 0)

    print(f'#{tc} ', end='')
    for result in range(H):
        print(f'{"".join(game_map[result])}')

'''
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)
'''
