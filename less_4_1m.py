# nominal = [20, 50, 100, 200]
# person = ['Тоголок Молдо', "К. Датка", "Т. Сатылганов", "А.Осмонов"]
#
# kg_dict = list(zip(nominal, person))
# print(kg_dict)

# c = 0
# while len(kg_dict) != len(person):
#     kg_dict[nominal[c]] = person[c]
#     c += 1
#
# for k, v in kg_dict.items():
#     print(f'{k}: {v}')
# print(kg_dict)

# countries = {
#     'kg': {'red', 'yellow'},
#     'ru': {'white', 'blue', 'red'},
#     'usa': {'white', 'blue', 'red'}
# }
# print(len(countries))
# while True:
#     color = input('введите цвет').split()
#     color = set(color)
#     for k, v in countries.items():
#         if not color - v:
#             print(k)
#         else:
#             print("нет такого цвета")




# print(kg.symmetric_difference(ru))
# print(kg ^ ru)
#
# print(kg.difference(ru))
# print(kg - ru)
#
# print(kg.intersection(ru))
# print(kg & ru)
#
# print(kg.union(ru))
# print(kg | ru)

# numbers = (1, 2, 3, 3, 3, 2, 4)
# numbers = set(numbers)
# print(numbers)
# print(type(numbers))



# dict = {key: value,}
# students = []
# candidates = [
#     {'name': 'Azat', 'OPT': 238},
#     {'name': 'Timur', 'OPT': 109},
#     {'name': 'Meerim', 'OPT': 137},
# ]
#
# for i in candidates:
#     if i['name'] == 'timur'.title():
#         students.append(i)
#     elif i['OPT'] >= 110:
#         students.append(i)
#     # else:
#     #     i['sled god'] = True
#
# for i in candidates:
#     print(i)
# print('\n')
# print(students)

student = {
    'name': 'Adilet',
    'age': 19,
    'height': 1.76,
    'hobby': ['english', 'football'],
    'active': True
}
student['hobby'].append('books')

print(student['hobby'][0])

#
#
# for k, v in student.items():
#     print(k, ':', v)
#
# print(student.keys())
# print(student.values())

# student2 = dict(name='Azamat', age=18, height=1.80)
# student.update(student2)
# print(type(student))

# print(student.get('name', 'не нашли!'))
# print(student['name'])







# student['weight'] = 80
# student['age'] = 20
#
# del student['age']
# a = student.pop('weight')
# print(a)
# print(student)


# students = ['sam', 'jack', 'azat', 'adilet']
#
# del_name = input('введите индекс или имя')
# if del_name in students:
#     students.remove(del_name)
# elif del_name.isnumeric():
#     del students[int(del_name)]
# print(students)

# print('04781'.isnumeric())
# students[0] = 'samat'
# print(students)

# old_name = input('old student')
# new_name = input('new student')
#
# students[students.index(old_name)] = new_name
# print(students)