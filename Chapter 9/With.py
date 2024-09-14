# To avoid the close() fncn burden we use with statement

with open("file.txt") as f :
    data = f.read()
print(data)