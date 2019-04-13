#default arguments
def add(x=0,y=0):
    #x = 12
    #y = 34
    z = x + y
    print(z)

def sub(x,y):
    z = x - y if x > y else y - x
    print(z)

add(12,6)
sub(5,10)
