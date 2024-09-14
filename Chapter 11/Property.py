class ch :
    @property
    def name(self) :
        return self.ename
    @name.setter
    def name (self,value) :
        self.ename=value

x=ch()
x.name="Harry"
print(x.name)