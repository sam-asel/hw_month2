mentors = []

while True:
    choice = input('1)Добавление 2)Изменение 3)Удаление\n выберите действие:')
    if choice == "1":
        print('Добавление')
        name = input('Введите имя!').title()
        if len(name) >=15:
            print('Слишком длинно!')
        elif len(mentors) >=5:
            mentors.pop(0)
            mentors.append(name)
        else:
            mentors.append(name)
    elif choice == "2":
        print('Изменение!')
        name = input('Введите имя!').title()
        if name in mentors:
            if len(name) >= 15:
                print('Слишком длинно!')
            else:
                mentors.remove(name)
                new = input('Введите имя!').title()
                mentors.append(new)
        else:
            print('Такого имени нет!')

    elif choice == "3":
        print('Удаление!')
        name = input('Введите имя!').title()
        if name in mentors:
            mentors.remove(name)
        else:
            print('Такого имени нет!')
    elif choice == "0":
        print("Выход!")
        break
    else:
        print("Такого действия нет!")
    print(mentors)

