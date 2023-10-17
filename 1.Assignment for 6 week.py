file_name = input("Enter the fiel name: ")
try:
    file_name = open(file_name)
except:
    print("File does not exist")
else:
    for line in file_name:
        print(line.upper().rstrip())
    file_name.close()