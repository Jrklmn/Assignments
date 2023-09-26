sum = 0
count = 0
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        num = int(number)
    except:
        print("invalid input,please enter a number: ")
        continue
    sum = sum + num
    count = count + 1
    average = sum / count
print("Sum of input numbers: ",sum)
print("number of input: ",count)
print("average of input numbers: ",average)

