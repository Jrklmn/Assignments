average = 0
listed = []
print("Typing 'done' will exit the program")
while True:
    try:
        numbers = input("Please enter a integer: ")
        if numbers == "done":
            print("Bye!!")
            break
        else:
            sum = 0
            numbers = int(numbers)
            listed.append(numbers)
            for items in listed:
                sum += items
            average = sum / len(listed)
            print(listed, ", average = ", "%.2f" % average)
    except ValueError:
        continue