file_name = open("mbox.txt","r")
count = 0
for line in file_name:
    if line.startswith("From:"):
        host_name = line.find("@")
        space = line.find("\n")
        print(line[host_name+1:space])
        count += 1
print('Total %d hosts printed'%count)
file_name.close()