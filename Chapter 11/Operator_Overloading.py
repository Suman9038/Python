class ch :
    def __init__(self,n) :
        self.n=n
    
    def __add__(num1,num2) :
        return num1.n + num2.n



n=ch(5)
m=ch(6)
print(n+m)