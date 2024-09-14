class c1 :
    a=1
    @classmethod
    def fun1(cls) :

        print(f"THE VAALUE OF THE CLASS IS {cls.a}")


c=c1()
c.a=67
c.fun1() # Ye instance attribute ka value nahi soo kiya q ki humne classmethod use kiya jise woo class attribute ka value hi show karega

