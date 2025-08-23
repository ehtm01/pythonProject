""" def add(a, b):
    return a + b """

""" a=3
b=4
c=add(a,b)
print(c) """

# print(add(3, 4))

""" def say():
    return 'hi'

print(say())

a = say()
print(a) """

""" def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result) """

""" def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result) """

""" def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3) """

""" def add_and_mul(a,b):
    return a+b, a*b

x = add_and_mul(3,4)
print(x)

a = input()

print(a) """

# input('숫자를 입력하세요 : ')

""" for i in range(19):
    print(i, end=" ")

for i in range(19):
    print(i) """

""" class FourCal():
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)

print(a.add()) """
