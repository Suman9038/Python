n= int(input("ENTER A NUMBER "))
for i in range(0,n) :
    for j in range(0,n) :
        if( i >= j) :
            print("*",end="") #End statement by default next line nahi jane deti
        else :
            print("",end="")
    print("\n")
    
    
    