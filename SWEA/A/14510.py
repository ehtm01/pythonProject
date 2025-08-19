# 14510. 나무 높이
T = int(input())

for x in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))
    date = 0
    height.sort()

    while len(set(height)) != 1:
        date += 1
        if height[-1] - height[0] == 2:
            if date % 2 == 0:
                height[0] += 2
            elif height[1] - height[0] == 1 and height[1] != height[-1]:
                height[1] += 1
        elif height[-1] - height[0] == 1:
            if date % 2 == 1:
                height[0] += 1
            elif height[1] - height[0] == 1 and height[1] != height[-1]:
                height[1] += 2
        else:
            if date % 2 == 0:
                height[0] += 2
            else:
                height[0] += 1
        height.sort()

    print(f'#{x} {date}')
