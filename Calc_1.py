def add(x,y):
    print("Addition called...")
    z = x + y
    print(z)

def sub(x,y):
    print("Subtraction Called...")
    z = x - y
    print(z)

def div(x,y):
    print("Division Called...")
    z = x / y
    print(z)

def mul(x,y):
    print("Multiplication Called...")
    z = x * y
    print(z)

def err(*args):
    print("Invalid Choice...")

while True:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    ch = input("Enter your choice : ")
    '''
    if int(ch) > 4:
        continue
    '''

    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))

    operations = {
        "1" : add,
        "2" : sub,
        "3" : div,
        "4" : mul
        }
    operations.get(ch, err)(x,y)
