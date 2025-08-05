T = int(input())

for test_case in range(1, T+1):
    num = list(map(int, input().strip()))

    arr = [0] * 12  # 자릿수 누적 리스트
    # 6개 입력값 위치 찾기
    for i in range(6):   
        arr[num[i]] += 1

    i = 0
    tri = r = 0
    while i < 10:   # i가 한 자리 양의 정수일 때 반복
        # triplet 조사
        if arr[i] >= 3: 
            arr[i] -= 3
            tri += 1
            continue
        # run 조사
        if arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
            r += 1
            continue
        i += 1

    if r + tri == 2:
        result ='Baby Gin'
    else:
        result = 'Lose'

    print(f'#{test_case} {result}')
