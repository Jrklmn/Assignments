while True:
    try: 
        input_str = input("Please enter two words: ") 
        if not input_str: 
            print("-- bye !!") 
            break
        if input_str == "done":
            print("-- bye !!") 
            break
        first, second = input_str.split() 
        listed = [first, second] 
        listed.sort() 
        print(listed[0], "comes first") 
    except ValueError:
        continue

