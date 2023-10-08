word = input("Enter a string: ")
upper = 0
lower = 0
digit = 0
other = 0
for i in word:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    else:
        other += 1
print("Uppercase letters :%s "%upper)
print("Lowercase letters :%s "%lower)
print("Numbers :%d "%digit)
print("Other characters :", other)