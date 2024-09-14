f = open("file.txt")

# data = f.readlines()

# print(data , type(data))

# readline

# line1 = f.readline()
# line2 = f.readline()

# print(line1)
# print(line2)

line = f.readline()
while(line != "") :
    print(line)
    line=f.readline()


f.close()
