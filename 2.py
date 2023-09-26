try:
    score = int(input("Enter your score: "))
except:
    print("Error!\nPlease enter numeric input between 0 and 100\n")
else:
    if score < 0 or score > 100:
        print("Error!\nPlease enter numeric input between 0 and 100\n")
    else:
        if score >= 90:
            print("A",end=" ")
        else:
            if score >= 80:
                print("B",end=" ")
            else:
                if score >= 70:
                    print("C",end=" ")
                else:
                    if score >= 60:
                        print("D",end=" ")
                    else:
                        print("F",end=" ")
        print("Grade")