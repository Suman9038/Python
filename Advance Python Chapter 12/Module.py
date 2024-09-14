def myFun() :
    print("HELLO WORLD I AM FROM ONE OF THE MODULE PART ")

if __name__ == "__main__" :
    print(" it is executed directly in module ")
    myFun()
    print(__name__)

else :
     myFun()
     print(__name__)