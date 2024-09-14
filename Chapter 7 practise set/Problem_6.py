n = int(input("ENTER A NUMBER"))
fact=1
for i in range (1,n+1) :
    if(n==0 or n==1) :
        print(f"THE FACTORIAL IS {1}")
        
    else :
        fact = fact*i
print(f"THE FACTORIAL OF NUMBER {n} iS {fact}")