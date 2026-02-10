# 1989. 초심자의 회문 검사

T = int(input())

for t in range(1, T+1):
    word = input()
    result = 1

    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            result = 0
            break

    print(f'#{t} {result}')
