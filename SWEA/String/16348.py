# 16348. 3일차 - 회문
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AYYvXypKDrkDFAVw&probBoxId=AZiHADjae2zHBINp&type=USER&problemBoxTitle=0808_String&problemBoxCnt=2


def find_sentence():
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            sentence = matrix[i][j:j+M]
            if sentence == sentence[::-1]:
                return sentence

    for j in range(N):
        col = [row[j] for row in matrix]
        for i in range(N - M + 1):
            sentence = ''.join(map(str, col[i:i+M]))
            if sentence == sentence[::-1]:
                return sentence


T = int(input())

for tc in range(1, T+1):
    result = find_sentence()
    print(f'#{tc} {result}')

