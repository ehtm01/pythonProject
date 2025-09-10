# SWEA 14229. 백만 개의 정수 정렬
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


arr = list(map(int, input().split()))
quick_sort(0, len(arr) - 1)
print(arr[500000])
