n = int(input("Enter the number : "))

'''
for i in range(1,11):
    #print(n*i)
    print("{} x {} = {}".format(n,i,n*i))
'''

'''
*
**
***
****
*****
'''
'''
for i in range(1,n):
    print(i * '*')
'''

'''
    *
   ***
  *****
 *******
*********
'''
for i in range(n):
    print(' ' * (n-i) + '*' * (2*i + 1))
















