num = input()

sco = list(map(int, input().split()))
sco.sort()

med = len(sco) // 2
print(sco[med])