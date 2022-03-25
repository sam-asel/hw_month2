a = list('аеёийоыуэюяaeiouy')
b = list("бвгджзклмнпрстфхцчшщbcdfghjklmnpqrstvwxz")
while True:
    words = input('Введите слово!').lower()
    count_glas =0
    count_cogl =0
    for word in words:
        if word in a:
            count_glas +=1
        if word in b:
            count_cogl +=1
    print(f'Слово:{words}\n'
          f'Количество букв:{len(words)}\n'
          f'Согласных букв:{count_cogl}\n'
          f'Гласных букв:{count_glas}\n'
          f'Гласные/Согласные:{count_glas/len(words)*100:2}%/{count_cogl/len(words)*100:2}%\n')

