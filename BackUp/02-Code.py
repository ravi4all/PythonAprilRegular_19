#by default input takes strings type of data
a = input("Enter your name : ")
msg = "hello "+a
print(msg)

#so we need to convert type of input
# we will do type casting/conversion
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
result = num_1 + num_2
print("Sum is",result)

result = num_1 - num_2
print("Diff is",result)

result = num_1 / num_2
print("Div is",result)

result = num_1 * num_2
print("Mul is",result)
