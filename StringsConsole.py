Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "my name is ravi and this is python programming"
>>> len(text)
46
>>> text[2]
' '
>>> text[5]
'm'
>>> text[-1]
'g'
>>> text[0:5]
'my na'
>>> text[5:10]
'me is'
>>> text[0:20:2]
'm aei aiad'
>>> text[0:20:4]
'maiaa'
>>> text[10:0]
''
>>> text[10:0:-1]
' si eman y'
>>> text[10::-1]
' si eman ym'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-10:-1]
'rogrammin'
>>> text[:]
'my name is ravi and this is python programming'
>>> text[:10]
'my name is'
>>> tex[0:]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tex[0:]
NameError: name 'tex' is not defined
>>> text[::-1]
'gnimmargorp nohtyp si siht dna ivar si eman ym'
>>> dir(str())
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text
'my name is ravi and this is python programming'
>>> text.upper()
'MY NAME IS RAVI AND THIS IS PYTHON PROGRAMMING'
>>> text.capitalize()
'My name is ravi and this is python programming'
>>> text.title()
'My Name Is Ravi And This Is Python Programming'
>>> text.count('i')
5
>>> text.index('i')
8
>>> text.find('i')
8
>>> text.find('i',9)
14
>>> text.find('i',15)
22
>>> text.find('i',23)
25
>>> text.find('i',89)
-1
>>> text.find('i',8)
8
>>> text.rfind('i')
43
>>> text.isdigit()
False
>>> text.islower()
True
>>> text.split()
['my', 'name', 'is', 'ravi', 'and', 'this', 'is', 'python', 'programming']
>>> x = ['my', 'name', 'is', 'ravi', 'and', 'this', 'is', 'python', 'programming']
>>> ' '.join(x)
'my name is ravi and this is python programming'
>>> '0'.join(x)
'my0name0is0ravi0and0this0is0python0programming'
>>> text
'my name is ravi and this is python programming'
>>> 
>>> text.replace('ravi','ram')
'my name is ram and this is python programming'
>>> text.replace(' ','ram')
'myramnameramisramraviramandramthisramisrampythonramprogramming'
>>> text.center(10)
'my name is ravi and this is python programming'
>>> text.center(20)
'my name is ravi and this is python programming'
>>> len(text)
46
>>> text.center(47)
' my name is ravi and this is python programming'
>>> text.center(48)
' my name is ravi and this is python programming '
>>> text.center(50)
'  my name is ravi and this is python programming  '
>>> text.center(60)
'       my name is ravi and this is python programming       '
>>> text.center(60,'*')
'*******my name is ravi and this is python programming*******'
>>> 
