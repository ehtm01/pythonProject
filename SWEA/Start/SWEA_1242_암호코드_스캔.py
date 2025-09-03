# SWEA 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔
import sys

sys.stdin = open('input.txt', 'r')

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

order = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9
}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    arrange = set()
    for _ in range(N):
        lst = input().strip()
        if lst != '0' * M:
            arrange.add(lst)

    values = set()
    for arr in arrange:
        binary = ''
        for n in arr:
            binary += hex_to_bin[n]
        prev = 0
        cnt = []
        for i in range(len(binary)):
            if binary[i] != binary[prev]:
                cnt.append(i - prev)
                prev = i

        nums = []
        for i in range(1, len(cnt), 4):
            min_num = min(cnt[i:i+3])
            order_key = str(cnt[i] // min_num) + str(cnt[i + 1] // min_num) + str(cnt[i + 2] // min_num)
            nums.append(order[order_key])

        test = []
        for i in range(0, len(nums), 8):
            values.add(tuple(nums[i: i+8]))

    result = 0
    for v in values:
        if (sum(v[0:7:2] * 3) + sum(v[1:8:2])) % 10 == 0:
            result += sum(v)

    print(f'#{tc} {result}')
