class Employee :
    lang = "Python" # ye sab ekk class attributes h ye class k liye h koi particular employee k liya nahi h 
    sal =  12000
    def __init__(self,name,lang,salary) :
        self.naaame=name
        self.lang=lang # sare insatance attribute create ho gaya
        self.sal=salary
        print("HEY FOLKS")
        
suman=Employee("SUMAN","PYTHON",2365523) # Object banaya h mtlb ek template ko suman naam ka employee fill up kiya h 
print(suman.naaame, suman.lang , suman.sal)