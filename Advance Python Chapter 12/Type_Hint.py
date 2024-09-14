from typing import List,Tuple,Union
# Variable bata sakte h konsa variable konsa daata type ka h
n : int = 6
n : str = "HARRY"
print(n)

#ise function mai v use kar skta h 
def fun(a : int , b : int) -> int  :
    return a+b


print(fun(3,5))

# Advance Typing Hints

#List of integer
numbers : list[int] = [1,3,6,4]

#Tupple of int and string 
person : Tuple[str,int] = ("SUMAN",89,"SAM")
print(person)

# Dictionary of string key and value as interger
s : dict[str,int] = {"sum" : 5, "hi" : 96, True : "how"}
print(s)

#Union of int and str
v : Union[int,str] = "1236ID"
print(v)