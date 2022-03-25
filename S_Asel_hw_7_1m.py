import random
import datetime
import time
a = random.randint(1, 100)
start = datetime.datetime.now()
popitka = 0
print(a)
while True:
    try:
        bet = int(input(f'Введите цифру!: '))
        popitka +=1
        if bet >=100 or bet <=0:
            print('Число должно быть от 1-100!')
            popitka-=1
        elif bet == a:
            print(f'Вы угадали число с попытки {popitka}')
            break
        elif bet < a:
            print('<')
        elif bet > a:
            print('>')
    except ValueError:
        print('Только числа!')
end = datetime.datetime.now() - start
print(f'время игры {end}')
