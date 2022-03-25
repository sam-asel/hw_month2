import calculate
from person import Person
from random import randint as generate_number
from datetime import date, datetime
from termcolor import colored, cprint


# import Person

print(calculate.addition(3,5))
print(calculate.sub(9, 5))
p1 = Person("Asel", 19)
print(p1)
print(generate_number(1, 30))
day_before_today = date(2022, 3, 15)
today = date.today()
# day = time.strftime("23.03.2022", "%d.%m.%Y")
print(f'Yesterday was: {day_before_today}')
print(f'Today was: {today}')
print(f'Day {time.strftime(today, "%d.%m.%Y %b")}')
print("23.03.2022")
# p1 = person.Person()
print(colored("python"))
# pip install- скачивает pip uninstall- удаляет
cprint("hello", "red","on yellow", attrs=['underline', 'on grey'])







# Первые три комманды пишутся только один раз когда вы делаете первый пуш
# git --version
# git config --global user.name "YOUR USERNAME ON GITHUB"
# git config --global user.email "YOUR EMAIL ON GITHUB"
# *
# git init
# git add .
# git status
# git commit -m "First Commit"
# git remote add origin <HTTPS link.git> - Remote тоже пишется единожды когда соединяем проект с репозиторем
# git branch
# git push -u origin master
#
# Когда вы все сделаете в след раз можете начинать с комманды
# git add .
# git status  (проверка нашего стэйжа)
# git commit -m "commit"
# git branch  (проверка на какой мы ветке)
# git push -u origin master
#
# потом скопируете мне ссылку вашего репозитория и отправите эту ссылку мне в личку телеграмма