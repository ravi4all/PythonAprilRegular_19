def add(*x):
    #print(x)
    count = 0
    for i in range(len(x)):
        count += x[i]
    print(count)

add(3,4,5,6)
add(7,8,9,6,5,2)
add(1,6,12,56,78,22)
