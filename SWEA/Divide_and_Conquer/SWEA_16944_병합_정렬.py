# SWEA 16944. 4일차 - 병합 정렬
import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def merge_sort(s, e):
    if s == e - 1:
        return s, e

    mid = (s + e) // 2
    left_s, left_e = merge_sort(s, mid)
    right_s, right_e = merge_sort(mid, e)

    merge(left_s, left_e, right_s, right_e)
    return s, e


def merge(l_s, l_e, r_s, r_e):
    global cnt
    if A[l_e - 1] > A[r_e - 1]:
        cnt += 1

    l, r = l_s, r_s
    N = r_e - l_s

    result = [0] * N
    idx = 0

    while l < l_e and r < r_e:
        if A[l] < A[r]:
            result[idx] = A[l]
            l += 1
            idx += 1
        else:
            result[idx] = A[r]
            r += 1
            idx +=1

    while r < r_e:
        result[idx] = A[r]
        r += 1
        idx += 1

    while l < l_e:
        result[idx] = A[l]
        l += 1
        idx += 1

    for i in range(N):
        A[l_s + i] = result[i]


for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    merge_sort(0, N)
    print(f'#{tc} {A[N // 2]} {cnt}')
