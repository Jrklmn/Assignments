def score_grade(score):
    if score < 0 or score > 100:
        return "Error!\nPlease enter numeric input between 0 and 100"
    elif score >= 90:
        return "Your grade is A"
    elif score >= 80:
        return "Your grade is B"
    elif score >=70:
        return "Your grade is C"
    elif score >=60:
        return "Your grade is D"
    elif score >= 0:
        return "Your grade is F"
    
if __name__ == "__main__":
    try:
        x=int(input("Enter Score: "))
    except:
        print("Error! Please enter numeric input between 0 and 100")
    else:
        result = score_grade(x)
        print("  ",result)