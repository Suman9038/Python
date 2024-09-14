n= int(input("ENTER A NUMBER : "))
for i in range(2,n) :
    if(n % i ) == 0 :
        print(" IT IS NOT PRIME ")
        break
else :
     print("IT IS PRIME NO")