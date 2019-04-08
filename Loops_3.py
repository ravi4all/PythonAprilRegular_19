'''
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
'''
num = int(input("Enter the number : "))
for i in range(1,11):
    #print(num * i)
    print("{} * {} = {}".format(num,i,num*i))
