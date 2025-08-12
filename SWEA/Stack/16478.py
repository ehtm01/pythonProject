# 16478. 4일차 - 반복문자 지우기
T = int(input())

for tc in range(1, T+1):
    top = -1
    N = 1000
    S = [0] * N
    sentence = input()
    l = len(sentence)

    for i in sentence:
        top += 1
        S[top] = i
        if S[top] == S[top - 1]:
            top -= 2

    print(f'#{tc} {top + 1}')
