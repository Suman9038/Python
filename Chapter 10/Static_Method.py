class Employee :
    lang = "Python" # ye sab ekk class attributes h ye class k liye h koi particular employee k liya nahi h 
    sal =  12000
    @staticmethod
    def greet() :
        print("good morning")

suman=Employee() # Object banaya h mtlb ek template ko suman naam ka employee fill up kiya h 
suman.greet()
print(suman.lang , suman.sal)