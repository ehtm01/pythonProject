# 24449. 야구 선수
def baseball(idx, d):
    global max_team
    if d > K:
        return

    if idx == N:
        max_team = N
        return

    max_team = max(max_team, len(team))
    team.append(player_value[idx])
    baseball(idx + 1, abs(team[0] - team[-1]))
    team.pop()


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    player_value = list(map(int, input().split()))
    player_value.sort()
    max_team = 1
    team = []
    baseball(0, 0)

    print(f'#{tc} {max_team}')
