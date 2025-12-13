# BAEK 2343. 기타 레슨
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 블루레이에는 총 N개의 강의
# i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화
# M개의 블루레이에 모든 기타 강의 동영상을 녹화
# 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 단, M개의 블루레이는 모두 같은 크기
# 강토의 각 강의의 길이가 분 단위(자연수)로 주어진다. 이때, 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 이분 탐색 범위 설정
start = max(arr)    # 블루레이 크기 최솟값
end = sum(arr)      # 블루레이 크기 최댓값
res = end           # 정답 후보

# 최솟값과 최댓값을 이용해 이분탐색
while start <= end:
    mid = (start + end) // 2    # 중간값
    cnt = 1     # 블루레이 갯수
    total = 0   # 블루레이 크기값

    # 중간값 크기로 강의 담아보기
    for a in arr:
        if total + a <= mid:
            total += a
        else:
            cnt += 1    # 블루레이 추가
            total = a

    # 블루레이 갯수 체크
    # 너무 많이 쓰면 최솟값을 키움
    if cnt > M:
        start = mid + 1
    # 아니면 최댓값을 줄임
    else:
        res = mid
        end = mid - 1

print(res)
