""" i = input()

a = int(i[0])
b = int(i[2])

if a-b > 0:
    print("A")
else:
    print('B')
 """

a, b = map(int, input().split())

if (a == 1 and b == 3) or \
   (a == 2 and b == 1) or \
   (a == 3 and b == 2):
    print("A")
else:
    print("B")