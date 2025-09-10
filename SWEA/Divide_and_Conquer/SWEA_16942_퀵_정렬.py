# SWEA 16942. 4일차 응용 - 퀵 정렬
import sys
sys.stdin = open("input.txt", "r")


def partition(s, e):
    pivot = arr[s]
    i = s + 1
    j = e

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[s], arr[j] = arr[j], arr[s]
    return j


def quick_sort(l, r):
    if l < r:
        pivot = partition(l, r)
        quick_sort(l, pivot - 1)
        quick_sort(pivot + 1, r)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N - 1)

    print(f'#{tc} {arr[N // 2]}')
