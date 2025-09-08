# BAEK 1931. 회의실 배정
N = int(input())
time = [[0] for _ in range(N)]
for t in range(N):
    s, e = map(int, input().split())
    time[t] = (e, s)

time.sort()
cnt = end = 0

for e, s in time:
    if s >= end:
        cnt += 1
        end = e

print(cnt)
