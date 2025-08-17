# 2806. N-Queen
def n_queen(row):   # 현재 행 입력
    global cnt      # 전역 변수 선언
    # 재귀함수 종료 -> n_queen 성공
    if row == N:
        cnt += 1
    # 재귀가 끝나지 않으면
    else:
        # N개의 열을 순회하며 반복
        for col in range(N):
            # 퀸을 놓을 수 있으면 True
            queen = True
            # 이전 행들을 순회하며 반복
            for r in range(row):
                # 대각선 판별: 행의 차이와 열의 차이가 같은 곳 ex) (2, 3), (0, 5) -> 행 차 2, 열 차 -2
                # 이전 행 중에서 1) 열이 겹치거나 2) 대각선이 겹치면
                if matrix[r] == col or abs(matrix[r] - col) == abs(r - row):
                    # 퀸을 놓을 수 없음 -> 반복 중단
                    queen = False
                    break
            # 퀸을 놓을 수 있으면 배열에 정보 저장 후 다음 행으로 재귀 실행
            if queen:
                matrix[row] = col
                n_queen(row + 1)
                # 만약 재귀가 끝나지 않고 다시 돌아오면 저장했던 정보 삭제(백트래킹)
                matrix[row] = -1


T = int(input())

for tc in range(1, T+1):
    # NxN, N개의 퀸 배치
    N = int(input())
    # n_queen 성공한 횟수 생성
    cnt = 0
    # 행과 열의 정보를 저장할 배열 생성
    # 값이 -1인 이유: matrix[행]의 값을 저장하면 열의 정보가 나오는데, 0~N-1까지의 값이기 때문이다.
    matrix = [-1] * N
    n_queen(0)

    print(f'#{tc} {cnt}')
