a = int(input("Enter the First number : "))
b = int(input("Enter the Second number : "))
if b==0 :
    raise ZeroDivisionError("It is not Possible")
else :
    print(a/b)