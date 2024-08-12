# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])  # e

# Loop through the letters in the word "banana":
for x in "banana":
    print(x)

# The len() function returns the length of a string:
a2 = "Hello, World!"
print(len(a2))  # 13

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)  # True

# Print only if "free" is present:
txt2 = "The best things in life are free!"
if "free" in txt2:
    print("Yes, 'free' is present.")

# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5 (not included):
b2 = "Hello, World!"
print(b2[:5])

# Get the characters from position 2, and all the way to the end:
b3 = "Hello, World!"
print(b3[2:])

a3 = "Hello, World!"
print(a3.upper())
