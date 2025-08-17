# 16530. 5일차 - Forth
T = int(input())

for tc in range(1, T+1):
    string = list(map(str, input().split()))
    N = len(string)
    stack = []
    a = 0
    b = 0

    for i in range(N):
        if string[i] in ('+', '-', '*', '/'):
            if len(stack) > 1:
                a = int(stack.pop())
                b = int(stack.pop())
                if string[i] == '+':
                    stack.append(b + a)
                elif string[i] == '-':
                    stack.append(b - a)
                elif string[i] == '*':
                    stack.append(b * a)
                elif string[i] == '/':
                    stack.append(b // a)
            else:
                stack = ['error']
                break
        elif string[i] == '.':
            break
        else:
            stack.append(string[i])
    if len(stack) > 1:
        stack = ['error']

    print(f'#{tc} {stack.pop()}')
