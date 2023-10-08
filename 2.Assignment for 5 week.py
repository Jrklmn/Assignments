word = input("Enter a string: ")
print("Input string = %s"%word)
index = 1
while index <= len(word):
    letter = word[-index]
    print(letter)
    index = index + 1