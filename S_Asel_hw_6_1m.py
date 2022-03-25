ten = [i for i in range(1, 11)]
print(ten)
evens = list(filter(lambda x: x%2 !=1, ten))
print(list(map(lambda x: x ** 2, evens)))
while 1:
    try:
       idx = int(input('Введите индекс!'))
       print(ten[idx])
    except ValueError:
        print('Вводите только цифры!')
    except IndexError:
        print('Вводите цифры щт 0 до 10')
    continue
    break
