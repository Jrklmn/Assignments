def num_divide3(x):
    count = 0
    for i in range(1,(int(x))+1):
        if i % 3 == 0:
            count += 1
    return count         

if __name__ == "__main__":
    while True:
        num=input("Enter a positive number: ")
        if num == 'done':
            break
        try:
            number = int(num)
            if number < 0:
                print("Please enter a positive number")
                continue
        except:
            print("Please enter a positive number")
        else:
            result = num_divide3(num)
            print("Numbers divisible by 3 among numbers from 1 to",num,": ",result)
    print("bye!!")