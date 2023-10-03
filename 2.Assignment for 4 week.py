def computepay(x,y):
    if y > 40:
        return 40 * x + (y-40)*1.5*x
    else:
        return x * y
if __name__ == "__main__":
    try:
        rate = int(input("Enter your rate: "))
        hours = int(input("Enter your hours: "))
    except:
        print("Error! please enter numeric input")
    else:
        result = computepay(rate,hours)
        print("Pay: ",result) 