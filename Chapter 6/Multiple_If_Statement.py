a=int(input("ENTER THE AGE : "))
# INDEPENDENT IF STATEMENT 1

if(a%2==0) :
    print("ENTERD AGE IS EVEN")

# FINISH OF IF STATEMENT

# ANOTHER IF STATEMENT WHICH IS NOT DEPENDENT ON FIRST IF STATEMNET

if(a>=18):
    print("YOU CAN VOTE")

elif(a<0) :
    print("THE AGE ENTERD IS INVALID")

elif (a==0) :
    print("YOU ENTERD THE AGE 0")

else :
    print("YOU ARE NOT ABOVE 18 YOU CANT VOTE")
