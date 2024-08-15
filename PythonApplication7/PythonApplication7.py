a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

a = "Hello"
b = "World"
c = a + b
print(c) # HelloWorld

a = "Hello"
b = "World"
c = a + " " + b 
print(c) # Hello World

# age = 36
# txt = "My name is John, I am " + age
# print(txt)

age = 36
txt = f"My name is John Connor, I am {age}"
print(txt) # My name is John Connor, I am 36

price = 59
txt = f"The price is {price} dollars"
print(txt) # The price is 59 dollars

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) # The price is 59.00 dollars

txt = f"The price is {20 * 59} dollars"
print(txt) # The price is 1180 dollars

txt = "We are the so-called \"Vikings\" from the north."

print(10 > 9)
print(10 == 9) # False
print(10 < 9) 

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 
  
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

x = 200
print(isinstance(x, int)) 

thislist = ["apple", "banana", "cherry"]
print(thislist) # ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # ['apple', 'banana', 'cherry', 'apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # <class 'list'>

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) # ['apple', 'banana', 'cherry']

# https://www.w3schools.com/python/python_lists_access.asp