# 16346. 3일차 - 문자열 비교
t = int(input())

for T in range(1, t+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    result = 0

    for i in range(M - N + 1):
        if str1[0] == str2[i]:
            for j in range(1, N):
                if str1[j] != str2[i+j]:
                    break
            else:
                result = 1

    print(f'#{T} {result}')
