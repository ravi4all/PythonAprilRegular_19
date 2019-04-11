Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers = [23,56,78,11,2,4,67,32]
>>> type(numbers)
<class 'list'>
>>> numbers = [23,56,78,11,2,4,67,32,12.34,11.33,"hello","hey"]
>>> numbers[0]
23
>>> numbers[1]
56
>>> numbers[5]
4
>>> numbers[0:5]
[23, 56, 78, 11, 2]
>>> numbers[0:10:2]
[23, 78, 2, 67, 12.34]
>>> numbers[-1]
'hey'
>>> numbers = []
>>> numbers.append(10)
>>> numbers
[10]
>>> numbers.append(20)
>>> numbers
[10, 20]
>>> numbers.append(30)
>>> numbers
[10, 20, 30]
>>> numbers.append(40)
>>> numbers
[10, 20, 30, 40]
>>> numbers = []
>>> for i in range(10,1001,10):
	numbers.append(i)

	
>>> numbers
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000]
>>> numbers.pop()
1000
>>> numberz
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    numberz
NameError: name 'numberz' is not defined
>>> numbers
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
>>> numbers = [10,20,50,21,22,4,5,34,56,78,32,55,53]
>>> list_2 = [12,14,15,66,23,67,87,43,24,67,77]
>>> numbers + list_2
[10, 20, 50, 21, 22, 4, 5, 34, 56, 78, 32, 55, 53, 12, 14, 15, 66, 23, 67, 87, 43, 24, 67, 77]
>>> numbers.extend(list_2)
>>> numbers
[10, 20, 50, 21, 22, 4, 5, 34, 56, 78, 32, 55, 53, 12, 14, 15, 66, 23, 67, 87, 43, 24, 67, 77]
>>> numbers.count(10)
1
>>> numbers.count(20)
1
>>> numbers.count(67)
2
>>> numbers.index(67)
18
>>> numbers.index(67, 19)
22
>>> numbers = [12,34,56,78,2,34,12,14,15,67,11,13,14,56,12,14,57]
>>> numbers.count(12)
3
>>> for i in range(len(numbers)):
	if numbers[i] == 12:
		print(numbers.index(12))

		
0
0
0
>>> numbers.index(12)
0
>>> for i in range(1,len(numbers)):
	if numbers[i] == 12:
		print(numbers.index(12))

		
0
0
>>> for i in range(1,len(numbers)):
	if numbers[i] == 12:
		print(i)

		
6
14
>>> for i in range(len(numbers)):
	if numbers[i] == 12:
		print(i)

		
0
6
14
>>> numbers
[12, 34, 56, 78, 2, 34, 12, 14, 15, 67, 11, 13, 14, 56, 12, 14, 57]
>>> numbers.insert(1,100)
>>> numbers
[12, 100, 34, 56, 78, 2, 34, 12, 14, 15, 67, 11, 13, 14, 56, 12, 14, 57]
>>> numbers.pop(5)
2
>>> numbers.remove(3)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    numbers.remove(3)
ValueError: list.remove(x): x not in list
>>> numbers.remove(34)
>>> sorted(numbers)
[11, 12, 12, 12, 13, 14, 14, 14, 15, 34, 56, 56, 57, 67, 78, 100]
>>> numbers
[12, 100, 56, 78, 34, 12, 14, 15, 67, 11, 13, 14, 56, 12, 14, 57]
>>> numbers.sort()
>>> numbers
[11, 12, 12, 12, 13, 14, 14, 14, 15, 34, 56, 56, 57, 67, 78, 100]
>>> numbers.sort(reverse  =True)
>>> numbers
[100, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> x = numbers
>>> x
[100, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> numbers
[100, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> numbers[0] = 99
>>> numbers
[99, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> x
[99, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> numbers[:]
[99, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> y = numbers[:]
>>> x
[99, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> y
[99, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> numbers
[99, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> numbers[0] = 100
>>> numbers
[100, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> x
[100, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> y
[99, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> y = numbers[:]
>>> x
[100, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> y
[100, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> numbers
[100, 78, 67, 57, 56, 56, 34, 15, 14, 14, 14, 13, 12, 12, 12, 11]
>>> x == y
True
>>> x == numbers
True
>>> numbers == y
True
>>> x is numbers
True
>>> x == y
True
>>> x is y
False
>>> emp = [['ram','shyam','gopal'],['IT','HR','IT'],[20000,30000,40000], 'TCS']
>>> emp[0]
['ram', 'shyam', 'gopal']
>>> emp[1]
['IT', 'HR', 'IT']
>>> emp[2]
[20000, 30000, 40000]
>>> emp[4]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    emp[4]
IndexError: list index out of range
>>> emp[3]
'TCS'
>>> emp_2 = emp[:]
>>> emp[3] = 'HCL'
>>> emp_3
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    emp_3
NameError: name 'emp_3' is not defined
>>> emp_2
[['ram', 'shyam', 'gopal'], ['IT', 'HR', 'IT'], [20000, 30000, 40000], 'TCS']
>>> emp
[['ram', 'shyam', 'gopal'], ['IT', 'HR', 'IT'], [20000, 30000, 40000], 'HCL']
>>> emp[0][0]
'ram'
>>> emp[1][0]
'IT'
>>> emp[2][0] = 25000
>>> emp
[['ram', 'shyam', 'gopal'], ['IT', 'HR', 'IT'], [25000, 30000, 40000], 'HCL']
>>> emp_2
[['ram', 'shyam', 'gopal'], ['IT', 'HR', 'IT'], [25000, 30000, 40000], 'TCS']
>>> import copy
>>> emp_3 = copy.deepcopy(emp)
>>> emp_3
[['ram', 'shyam', 'gopal'], ['IT', 'HR', 'IT'], [25000, 30000, 40000], 'HCL']
>>> emp_2
[['ram', 'shyam', 'gopal'], ['IT', 'HR', 'IT'], [25000, 30000, 40000], 'TCS']
>>> emp
[['ram', 'shyam', 'gopal'], ['IT', 'HR', 'IT'], [25000, 30000, 40000], 'HCL']
>>> emp == emp_3
True
>>> emp[0][0] = 'Raman'
>>> emp
[['Raman', 'shyam', 'gopal'], ['IT', 'HR', 'IT'], [25000, 30000, 40000], 'HCL']
>>> emp_2
[['Raman', 'shyam', 'gopal'], ['IT', 'HR', 'IT'], [25000, 30000, 40000], 'TCS']
>>> emp_3
[['ram', 'shyam', 'gopal'], ['IT', 'HR', 'IT'], [25000, 30000, 40000], 'HCL']
>>> print(emp[0][0], emp[1][0], emp[2][0], emp[3])
Raman IT 25000 HCL
>>> print(emp[0][1], emp[1][1], emp[2][1], emp[3])
shyam HR 30000 HCL
>>> len(emp[0])
3
>>> for i in range(len(emp[0])):
	print(emp[0][i], emp[1][i], emp[2][i], emp[3])

	
Raman IT 25000 HCL
shyam HR 30000 HCL
gopal IT 40000 HCL
>>> 
