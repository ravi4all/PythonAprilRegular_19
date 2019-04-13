'''
*args
**kwargs
'''
'''
def emp(id, name, sal, *address):
    print("Id : {}".format(id))
    print("Name : {}".format(name))
    print("Sal : {}".format(sal))
    print("Address : {}".format(address))

emp(101,'Ram', 34000, 'Delhi')
emp(102, 'Shyam', 23000, 'Pune', 'Delhi')
emp(103, 'Mohan', 45000, 'Pune', 'Mumbai', 'Delhi')
'''

def emp(**details):
    print(details)

emp(name='Ram', sal=45000,dept='IT')
emp(id=101,name='Shyam',dept = 'IT', address = 'Delhi')
emp(id=101,name='Raman',dept = 'IT', address = 'Pune',sal=56000)
