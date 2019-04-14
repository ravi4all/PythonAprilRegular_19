def calc(x,y, opr):
    expression = x + opr + y
    result = eval(expression)
    print(result)

def err(*args):
    print("Invalid Choice...")

def main():
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

        x = input("Enter first number : ")
        y = input("Enter second number : ")

        operations = {
            "1" : "+",
            "2" : "-",
            "3" : "/",
            "4" : "*",
            }
        opr = operations.get(ch)
        calc(x,y,opr)

main()
