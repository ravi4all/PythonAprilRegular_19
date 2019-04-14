def outer():
    x = 12
    y = 22
    def inner_1():
        z = x + y
        return z
    def inner_2():
        z = x - y
        return z
    #return inner_1()
    return inner_1, inner_2

#x = outer()
#print(x())
#print(x[0]())

x = outer()[1]()
print(x)
