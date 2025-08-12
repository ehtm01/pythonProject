# 16476. 4일차 - 괄호검사
t = int(input())

for T in range(1, t+1):
    tc = input()
    top = -1
    N = len(tc)
    s = [0] * N
    dict = {'(': ')', '{': '}'}

    result = 1
    for i in tc:
        if i in dict:
            top += 1
            s[top] = i
        if i in dict.values():
            if top == -1:
                result = 0
                break
            if dict[s[top]] != i:
                result = 0
                break
            top -= 1
    else:
        pass

    if top != -1:
        result = 0

    print(f'#{T} {result}')
