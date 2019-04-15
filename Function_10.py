def even(n):
    return n % 2 == 0

#e = even(10)
#print(e)

numbers = list(range(1,101))

'''
e = list(map(even, numbers))
print(e)
'''
'''
e = []
for i in range(len(numbers)):
    if even(numbers[i]):
        e.append(numbers[i])
print(e)
'''

'''
e = list(filter(even, numbers))
print(e)
'''

e = list(filter(lambda x : x % 2 == 0, numbers))
print(e)
