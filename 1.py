try:
    rate = int(input("Enter your rate: "))
    hours = int(input("Enter your hours: "))
except:
    print("Error, please enter a numeric input")
else:
    if hours > 40:
        salary = 40 * rate + (hours - 40) * 1.5 * rate
        print("Your salary is=",salary)
    else:
        if hours <= 40:
            salary = rate * hours
            print("Your salary is=",salary)
