
x = "awesome and pythonic"


def myfunc():
    global x
    x = "fantastic and can be used for data science."


myfunc()

print("Python is " + x)

x2 = 5
print(type(x2))

x3 = 1j  # complex

x4 = ["apple", "banana", "cherry"]  # list

x5 = ("apple", "banana", "cherry")  # tuple

x6 = range(6)
print(x6)

x7 = {"name": "John", "age": 36}  # dict

x8 = {"apple", "banana", "cherry"}  # set

x10 = True

x11 = 1  # int
y11 = 2.8  # float
z11 = 1j  # complex

# convert from int to float:
a = float(x11)

# convert from float to int:
b = int(y11)

# convert from int to complex:
c = complex(x11)

print(a)
print(b)
print(c)  # (1+0j)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))