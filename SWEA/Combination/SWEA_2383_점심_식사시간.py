# SWEA 2383. [모의 SW 역량테스트] 점심 식사시간
from collections import deque
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    stair = []
    people = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 1:
                stair.append((i, j, matrix[i][j]))
            elif matrix[i][j] == 1:
                people.append((i, j))
    # 부분 집합 이용하면 좋을듯
    def comb():
        


    # s1_r, s1_c = stair[0][0], stair[0][1]
    # s2_r, s2_c = stair[1][0], stair[1][1]
    # time_to_1 = []
    # time_to_2 = []
    # for p in people:
    #     if abs(p[0] - s1_r) + abs(p[1] - s1_c) < abs(p[0] - s2_r) + abs(p[1] - s2_c):
    #         time_to_1.append(abs(p[0] - s1_r) + abs(p[1] - s1_c))
    #     elif abs(p[0] - s1_r) + abs(p[1] - s1_c) > abs(p[0] - s2_r) + abs(p[1] - s2_c):
    #         time_to_2.append(abs(p[0] - s2_r) + abs(p[1] - s2_c))
    #     else:
    #         if stair[0][2] < stair[1][2]:
    #             time_to_1.append(abs(p[0] - s1_r) + abs(p[1] - s1_c))
    #         elif stair[0][2] > stair[1][2]:
    #             time_to_2.append(abs(p[0] - s2_r) + abs(p[1] - s2_c))
    #         else:
    #             if len(time_to_1) <= len(time_to_2):
    #                 time_to_1.append(abs(p[0] - s1_r) + abs(p[1] - s1_c))
    #             else:
    #                 time_to_2.append(abs(p[0] - s2_r) + abs(p[1] - s2_c))
    #
    # time_to_1.sort()
    # time_to_2.sort()
    # print(time_to_1, stair[0][2], time_to_2, stair[1][2])
    #
    # def move():
    #     q1 = deque()
    #     q2 = deque()
