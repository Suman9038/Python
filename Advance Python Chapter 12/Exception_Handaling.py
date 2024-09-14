try :
    a=int(input("Enter a number : "))
    print(a)

except ValueError :
    print ("HEY PLEASE ENTER PROPERLY")

except Exception :
    print("Please enter properly as it ask for integer input")
