import random
import date
name = input("Введитe имя!: ")
ats = int(input("Количество попыток?: ")) # ats= attempts
start = datetime.datetime.now()
vse = ats
with open('results.txt', 'a') as file:
        while ats !=0:
            try:
                one = random.randint(1, 9)
                two = random.randint(1, 9)
                numbers = one * two
                ats -= 1
                otvet = int(input(f"{one} * {two} = ?  "))
                print(numbers)
                c = f'{one} * {two} = {otvet} ,({numbers})'
            except TypeError:
                print("Буквы нельзя, только цифры!")
            if otvet == numbers:
                     file.write(f"\n {c} правильно!")
            elif numbers != otvet:
                     file.write(f"\n {c} неправильно!")
        end = datetime.datetime.now() - start

        file.write(f'\n Было {vse} попыток, потраченное время: {end} , имя: {name}')
