# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


new_students = {}


for list in students:
    stud_name = list['first_name']
    if stud_name in new_students:
        new_students[stud_name] = new_students.get(stud_name) + 1
    else:
        new_students[stud_name] = 1

for name, recur in new_students.items():
    print(name, recur)



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Петя'},
]


new_students = {}


for list in students:
    stud_name = list['first_name']
    if stud_name in new_students:
        new_students[stud_name] = new_students.get(stud_name) + 1
    else:
        new_students[stud_name] = 1


name_recur = 0


for user in new_students:
    if new_students[user] > name_recur:
        name_recur = new_students[user]
        user_names = user


print(f'Самое частое имя среди учеников: {user_names}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


for one_class in school_students:
    class_students = {}
    for dict in one_class:
        name_class = dict['first_name']
        if name_class in class_students:
            class_students[name_class] = class_students.get(name_class) + 1
        else:
            class_students[name_class] = 1
    print(class_students)

    name_recur = 0

    for name_stud in class_students:
        if class_students[name_stud] > name_recur:
            name_recur = class_students[name_stud]
            print(f'Самое частое имя в классе №: {name_stud}') # не понимаю как прилично здесь вывести номер класса

#    for class_num, class_students in enumerate(class_students, start=1):
#        print(f'Самое частое имя в классе {class_num}: {name_stud}')



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

