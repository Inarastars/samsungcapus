#дан кортеж, надо перенести все значение с словарь
#student_tup = (('211101', 'David Doe', '010-1234-4500'),
#               ('211102', 'John Smith', '010-2230-6540'),
#               ('211103', 'Jane Carter', '010-3232-7788'))
#student_dic = {}
#for i in range(len(student_tup)):
#    arr = []
#    student_id = student_tup[i][0]
#    arr.append(student_tup[i][1])
#    arr.append(student_tup[i][2])
#    student_dic[student_id] = arr
#print(student_dic)

#используя кортеж из предыдущей задачи, надо написать айди студента чтобы получить билет
#student_tup = (('211101', 'David Doe', '010-1234-4500'),
#               ('211102', 'John Smith', '010-2230-6540'),
#               ('211103', 'Jane Carter', '010-3232-7788'))
#student_dic = {}
#for i in range(len(student_tup)):
#    arr = []
#    student_id = student_tup[i][0]
#    arr.append(student_tup[i][1])
#    arr.append(student_tup[i][2])
#    student_dic[student_id] = arr

#user_ticket = input("Enter student ID: ")
#if user_ticket in student_dic:
#    print(f"Name:", student_dic[user_ticket][0])
#    print(f"Phone number:", student_dic[user_ticket][1])
#else:
#    print("Student ID not found")

student_tup = [('211101', 'David Doe', '010-1234-4500'),
               ('211102', 'John Smith', '010-2230-6540'),
               ('211103', 'Jane Carter', '010-3232-7788')]
student_dic = {}
for i in range(len(student_tup)):
    arr = []
    student_id = student_tup[i][0]
    arr.append(student_tup[i][1])
    arr.append(student_tup[i][2])
    student_dic[student_id] = arr
    print(f"{student_id} : {student_tup[i][1]}")

a = input("Enter student ID number: ")
if a in student_dic:
    value = student_dic[a]
    print(f"{student_id} student is {value[0]} and phone number is {value[1]}")