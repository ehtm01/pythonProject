for test_case in range(1, 11):  # 테스트 케이스 = 10
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0  # 결과값 생성
    # 양 끝 높이가 0인 빌딩 2개는 순회 목록에서 제외
    for i in range(2, N-2):
        # 양 옆 2개의 빌딩과 높이 비교
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2]:
            if buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
                # 양 옆의 빌딩 중 가장 높은 빌딩의 높이와 그 빌딩들과 현재 비교 중인 빌딩의 높이 차 계산
                left_height = 0
                right_height = 0
                diff_height = 0
                left_height = max(buildings[i-1], buildings[i-2])
                right_height = max(buildings[i+1], buildings[i+2])
                diff_height = buildings[i] - max(left_height, right_height)
                # 조망이 좋은 칸 모두 더함
                result += diff_height

    print(f'#{test_case} {result}')
