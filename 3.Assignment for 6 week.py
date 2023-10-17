file_name = input("Enter the file name: ")
count = 0
sum = 0
try:
    f_name = open(file_name)
    for line in f_name:
        if line.startswith("X-DSPAM-Confidence:"):
             spam_num = float(line.split(':')[-1])
             sum = sum + spam_num
             count += 1
    if count > 0:
        average = sum / count
        print("Average spam confidence:%f"%average)
    f_name.close()    
except:
    print("File cannot be opened:%s"%file_name)

