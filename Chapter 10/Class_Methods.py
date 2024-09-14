class Employee :
    lang = "Python" # ye sab ekk class attributes h ye class k liye h koi particular employee k liya nahi h 
    sal =  12000

    def getInfo(self) :
     print (f"This Employee use {self.lang} programing and he has a salary of {self.sal}")

    def greet(self) :
       print("GOOD MORNING")
    

suman =  Employee() # Object banaya h mtlb ek template ko suman naam ka employee fill up kiya h 
suman.greet()
suman.getInfo() # jaisa ye call karnge ek error throw karega ki ek parameter pass karna hoga q ki method mai ek parameter h 
#Employee.getInfo(suman) # ye us call ko isme convert kar dega and isme ek paarameter h toh hume method mai ek "self" parameter pass karna hota h 
print(suman.lang , suman.sal)