fhand = open("romeo.txt","r")
new_list = list()
for line in fhand:
    text = line.split()
    for word in text:
        if word not in new_list:
            new_list.append(word)
new_list.sort()
print(new_list)
fhand.close()              