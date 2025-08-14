# 16530. 5일차 - Forth
T = int(input())

for tc in range(1, T+1):
    string = list(map(str, input().split()))
    N = len(string)
    stack = []
    a = 0
    b = 0

    for i in range(N):
        if string[i] not in ('+', '-', '*', '/'):
            stack.append(string[i])
        elif string[i] == '.':
            print(f'#{tc} {stack.pop()}')
        else:
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

    print(f'#{tc} {stack.pop()}')