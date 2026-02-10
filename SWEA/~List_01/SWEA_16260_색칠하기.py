# SWEA 16260. 2일차 - 색칠하기
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     red_case = []   # 빨강 칸 리스트
#     blue_case = []  # 파랑 칸 리스트
#     for i in range(N):  # 칠하는 영역 수만큼 반복
#         r1, c1, r2, c2, color = map(int, input().split())   # 입력값 분리
#         # x좌표 차이(가로 길이)만큼 반복
#         for j in range(r1, r2+1):
#             # y좌표 차이(세로 길이)만큼 반복
#             for k in range(c1, c2+1):
#                 if color == 1:  # 빨강이면
#                     red_case.append((j, k))     # 빨강 칸 리스트에 추가
#                 else:   # 파랑이면
#                     blue_case.append((j, k))    # 파랑 칸 리스트에 추가
#     # 같은 색 사각형이 겹치면 세트로 중복 제거
#     red_square = set(red_case)
#     blue_square = set(blue_case)
#     # 교집합으로 출력값 도출
#     print(f'#{test_case} {len(red_square & blue_square)}')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    M = 10
    cnt = 0
    matrix = [[0] * M for _ in range(M)]

    for square in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if color == 1:
                    if matrix[i][j] == 2:
                        cnt += 1
                    else:
                        matrix[i][j] = 1
                else:
                    if matrix[i][j] == 1:
                        cnt += 1
                    else:
                        matrix[i][j] = 2

    print(f'#{tc} {cnt}')
