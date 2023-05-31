# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


print('Ответ на задание 1:')


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


repeat_students = {}


for inform_student in students:
    student_name = inform_student['first_name']
    if student_name in repeat_students:
        repeat_students[student_name] = repeat_students.get(student_name) + 1
    else:
        repeat_students[student_name] = 1


for name, count_name in repeat_students.items():
    print(name, count_name)


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша


print('Ответ на задание 2:')


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


number_repetitions_names = {}


for inf_student in students:
    student_name = inf_student['first_name']
    if student_name in number_repetitions_names:
        number_repetitions_names[student_name] = number_repetitions_names.get(student_name) + 1
    else:
        number_repetitions_names[student_name] = 1


max_key = max(number_repetitions_names, key=number_repetitions_names.get)
print(f'Самое частое имя среди учеников: {max_key}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


print('Ответ на задание 3:')


school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'}
    ],[  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'}
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'}
    ],
]


count_name = 0


for class_num, every_class in enumerate(school_students, start=1):
    class_students = {}
    for every_schoolkid in every_class:
        if every_schoolkid['first_name'] in class_students:
            count_name += 1
            class_students[every_schoolkid['first_name']] = count_name
        else:
            count_name = 1
            class_students[every_schoolkid['first_name']] = count_name

    max_repeat = max(class_students, key=class_students.get)
    print(f'Самое частое имя в классе {class_num}: {max_repeat}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2


print('Ответ на задание 4:')


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


for inform_class in school:
    class_num = inform_class['class']
    if inform_class.get('students'):
        students = inform_class['students']
        count_man = 0
        count_women = 0
        
        for name_stud in students:
            name_gender = name_stud['first_name']
            if name_gender in is_male:
                gender = is_male[name_gender]
                if gender:
                    count_man += 1
                else:
                    count_women += 1
            else:
                print(f'У {name_gender} не обозначен пол')
                count_women = "Ошибка"
                count_man = "Ошибка"
                break
    print(f'Класс {class_num}: девочки {count_women},  мальчики {count_man}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a


print('Ответ на задание 5:')


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


sum_gender_in_scool =[]


for inform_class in school:
    num_gender_in_class = {}
    class_num = inform_class['class']
    num_gender_in_class['class'] = class_num
    if inform_class.get('students'):
        students = inform_class['students']
        count_women = 0
        count_man = 0

        for name_students in students:
            name_gender = name_students['first_name']
            if name_gender in is_male:
                gender = is_male[name_gender]
                gender_list = {}
                if gender:
                    count_man += 1
                else:
                    count_women += 1
            else:
                print(f'У {name_gender} не обозначен пол')
                count_women = "Ошибка"
                count_man = "Ошибка"
                break
        gender_list['девочки'] = count_women
        gender_list['мальчики'] = count_man
        num_gender_in_class['gender'] = gender_list
        sum_gender_in_scool.append(num_gender_in_class)
    

        

for inform_every_class in sum_gender_in_scool:
    num_class = inform_every_class.get('class')

    if inform_every_class.get('gender'):
        gender_lists = inform_every_class['gender']
        max_gender = max(gender_lists, key=gender_lists.get)

    if max_gender == 'девочки':
        print(f'Больше всего девочек в классе {num_class}')
    elif max_gender == 'мальчики':
        print(f'Больше всего мальчиков в классе {num_class}')
