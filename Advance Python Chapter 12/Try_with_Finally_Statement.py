def main() :
    try :
        a=int(input("Enter a number : "))
        print(a)
        return

    except Exception :
        print("Please enter properly as it ask for integer input")
        return

    finally :
        print("THANK YOU")

main()

