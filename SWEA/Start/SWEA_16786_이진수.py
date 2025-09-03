# SWEA 16786. 1일차 응용 - 이진수
T = int(input())

for tc in range(1, T + 1):
    N, hex_string = input().split()

    N = int(N)

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

    result_bin = ''

    # for n in hex_string:
    #     result_bin += hex_to_bin[n]
    #
    # print(f'#{tc} {result_bin}')

    # 비트 사용
    for c in hex_string:
        # c => 16진수 문자열
        # 16진수 문자열 c를 숫자로 변환
        hex_c = int(c, 16)
        print(hex_c)
        # 16진수 => 2진수 4개
        for i in range(3, -1, -1):
            if (1 << i) & hex_c:
                result_bin += '1'
            else:
                result_bin += '0'

    print(result_bin)