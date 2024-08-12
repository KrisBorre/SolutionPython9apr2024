x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x1 = "awesome"


def myfunc1():
    print("Python is " + x1)


myfunc1()

x2 = "awesome"


def myfunc():
    x2 = "fantastic"
    print("Python is " + x2)


myfunc()

print("Python is " + x2)

"""
Python is awesome
Python is awesome
Python is awesome
15
5 John
Python is awesome
Python is fantastic
Python is awesome
"""

def myfunc():
  global x3
  x3 = "fantastic, readable and clean."

myfunc()

print("Python is " + x3)