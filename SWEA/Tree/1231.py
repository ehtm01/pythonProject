# 1231. [S/W 문제해결 기본] 9일차 - 중위순회
def inorder(t):
    global result

    if t:
        inorder(int(c_l[t]))
        result += tree[t]
        inorder(int(c_r[t]))


T = 10

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    c_l = [0] * (N + 1)
    c_r = [0] * (N + 1)
    result = ''

    for i in range(1, N + 1):
        arr = input().split()
        if len(arr) == 4:
            c_r[i] = arr[3]
            c_l[i] = arr[2]
        else:
            if len(arr) == 3:
                c_l[i] = arr[2]
        tree[i] = arr[1]

    inorder(1)
    print(f'#{tc} {result}')
