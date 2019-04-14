#Return Statement
def calc(x,y):
    z = x + y
    z1 = x - y
    z2 = x / y
    z3 = x * y
    #print(z)
    return z,z1,z2,z3

a,*b = calc(3,4)
print(a,b)
