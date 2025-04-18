#Создайте кортеж из 7-ми именованных кортежей учащихся одной школы. В именованном кортеже будут присутствовать следующие поля: имя школьника, возраст, оценка за четверть, город проживания. Функция good_students() будет принимать этот кортеж, вычислять среднюю оценку по всем учащимся и выводить на печать следующее сообщение: "Ученики {список имен студентов через запятую} в этой четверти хорошо учатся!". В список учеников, которые выводятся по результатам работы функции, попадут лишь те, у которых оценка за четверть равна или выше средней по всем учащимся.
from collections import namedtuple
Student = namedtuple("Student", ["name", "age", "grade", "city"])
Students = (
    Student("Амина", 13, 4, "Алматы"),
    Student("Алина", 17, 3, "Астана"),
    Student("Инкар", 10, 5, "Шымкент"),
    Student("Дмитрий", 9, 3, "Туркестан"),
    Student("Елена", 16, 4, "Алматы"),
    Student("Василиса", 13, 5, "Москва"),
    Student("Диана", 14, 5, "Ташкент"),
)
def good_students(students):
    avg_grade = sum(student.grade for student in students) / len(students)
    good_students_list = [student.name for student in students if student.grade >= avg_grade]
    print(f"Ученики {', '.join(good_students_list)} в этой четверти хорошо учатся!")
good_students(Students)

#Дан словарь d = {'1': 1.29, '2': 0.43}. Используя доступ к элементам словаря по ключу, найдите произведение 1.29*0.43, после чего добавьте результат в словарь, а затем выведите значение нового элемента на экран.
d = {'1': 1.29, '2': 0.43}
proizvedenie = d['1'] * d ['2']
d['3'] = proizvedenie
print(d['3'])

#Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
n, m = map(int, input().split())  # Явно преобразуем input в два числа
b = [["." if (i + j) % 2 == 0 else "*" for j in range(m)] for i in range(n)]
for row in b:
    print("".join(row))
