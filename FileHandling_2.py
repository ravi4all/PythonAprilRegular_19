file = open('file_1.txt')

#data = file.read(10)

#file.seek(10)
#data = file.read()

#data = file.readline()

data = file.readlines()
print(data)

file.close()
