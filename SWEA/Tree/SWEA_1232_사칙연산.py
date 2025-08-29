# SWEA 1232. [S/W 문제해결 기본] 9일차 - 사칙연산
def postorder(t):
    if tree[t] in operator:
        postorder(c_l[t])
        postorder(c_r[t])
        cal(t)


def cal(n):
    x, y = float(tree[c_l[n]]), float(tree[c_r[n]])
    if tree[n] == '+':
        tree[n] = x + y
    elif tree[n] == '-':
        tree[n] = x - y
    elif tree[n] == '*':
        tree[n] = x * y
    elif tree[n] == '/':
        tree[n] = x / y


T = 10
operator = ['+', '-', '*', '/']

for tc in range(1, T + 1):
    N = int(input())
    c_l = [0] * (N + 1)
    c_r = [0] * (N + 1)
    tree = [0] * (N + 1)
    for i in range(1, N + 1):
        arr = list(map(str, input().split()))
        tree[i] = arr[1]
        if len(arr) > 2:
            c_l[i] = int(arr[2])
            c_r[i] = int(arr[3])

    postorder(1)
    print(f'#{tc} {int(tree[1])}')
