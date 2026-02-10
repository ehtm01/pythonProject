N = input()
i = len(N) - 1
j = 0

while i >= 0:
    j += int(N[i])
    i -= 1

print(j)