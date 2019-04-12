data = [
    {'s_id':101,'s_name':'Aman','s_grade':'A','s_marks':[67,65,78]},
    {'s_id':102,'s_name':'Raman','s_grade':'A+','s_marks':[77,55,68]},
    {'s_id':103,'s_name':'Amit','s_grade':'A','s_marks':[62,60,70]},
    {'s_id':104,'s_name':'Ramesh','s_grade':'B','s_marks':[45,55,68]},
    {'s_id':105,'s_name':'Ram','s_grade':'B+','s_marks':[48,78,98]},
    {'s_id':106,'s_name':'Shyam','s_grade':'A','s_marks':[93,95,98]},
    {'s_id':107,'s_name':'Sita','s_grade':'A+','s_marks':[89,87,78]},
    {'s_id':108,'s_name':'Geeta','s_grade':'B+','s_marks':[66,63,70]},
    ]
'''
for i in range(len(data)):
    if data[i]['s_name'].startswith('A'):
        print(data[i]['s_name'], data[i]['s_marks'])
'''
'''
for i in range(len(data)):
    if data[i]['s_grade'] == 'A+':
        print(data[i]['s_name'], data[i]['s_grade'], data[i]['s_marks'])
'''
for i in range(len(data)):
    avg = sum(data[i]['s_marks']) // len(data[i]['s_marks'])
    print(data[i]['s_name'], " => ", avg)
