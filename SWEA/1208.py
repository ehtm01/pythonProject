def bubble_sort(a, n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def counting_sort(data, k=100):
    counts = [0] * (k+1)
    temp = [0] * len(data)

    for i in range(len(data)):
        counts[data[i]] += 1

    for i in range(1, k+1):
        counts[i] += counts[i-1]

    for i in range(len(data)-1, -1, -1):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]

    return temp


for test_case in range(1, 11):
    dump_count = int(input())
    height = list(map(int, input().split()))
    sorted_height = counting_sort(height)

    for dump in range(dump_count):
        sorted_height[0] += 1
        sorted_height[-1] -= 1
        bub_sorted_height = bubble_sort(sorted_height, len(sorted_height))
        sorted_height = bub_sorted_height

    print(f'#{test_case} {sorted_height[-1] - sorted_height[0]}')
