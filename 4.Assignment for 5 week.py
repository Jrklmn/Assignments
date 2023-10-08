while True:
    word = input("Please enter a string: ")
    char_remov = [':', ',', '.', ';', '!', '?']
    if word == "done":
        print("Bye !")
        break
    for i in word:
        if i in char_remov:
            word = word.replace(i, '')
    print(' '.join((word.upper()).split()))