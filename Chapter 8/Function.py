# Function defination
def func1() :
    print("HELLO")

def fun2(name) :
    print(f"GOOD MORNING , {name}")


def fun3(name,end) :
    print(f"GOOD MORNING , {name}")
    print(end)


def fun4(name,end="SOO NA BETA") :
    print(f"GOOD MORNING , {name}")
    print(end)

func1() # Function calling
fun2("SUM")
fun3("SUM","SOO JOA")
fun4("SUAMAM ") # Kuch pass nahi karenge toh jo default argument h wahi kaam karega 
fun4("SAMAMA","SO JAO") # isme jo passss kiya h argument wahi kaaam karega