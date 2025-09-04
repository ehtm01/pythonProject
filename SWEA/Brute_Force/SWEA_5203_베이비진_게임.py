# SWEA 5203. 베이비진 게임
import sys
sys.stdin = open("input.txt", "r")


def is_baby_gin(arr):
    global result

    for i in range(len(arr) - 2):
        if arr[i] == arr[i + 1] == arr[i + 2]:
            result = True
            return
        elif arr[i] + arr[i + 2] == arr[i + 1] * 2 and arr[i] + 1 == arr[i + 1]:
            result = True
            return


def perm(arr, n):
    global result

    if n == len(arr):
        is_baby_gin(path)
        return

    for i in range(len(arr)):
        if used[i] == True:
            continue
        used[i] = True
        path.append(arr[i])
        perm(arr, n + 1)
        path.pop()
        used[i] = False
        if result == True:
            return


T = int(input())

for tc in range(1, T + 1):
    number = list(map(int, input().split()))
    nums_1 = []
    nums_2 = []
    path = []
    used = [False] * 12
    result = False
    for i in range(12):
        if i % 2 == 0:
            nums_1.append(number[i])
            if len(nums_1) >= 3:
                perm(nums_1, 0)
                if result == True:
                    print(f'#{tc} 1')
                    break
        else:
            nums_2.append(number[i])
            if len(nums_2) >= 3:
                perm(nums_2, 0)
                if result == True:
                    print(f'#{tc} 2')
                    break
    else:
        print(f'#{tc} 0')
