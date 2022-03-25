movies = {}

def add_movies(name):
    if name in movies.keys():
        print('This movie allredy exist')
    else:
        movies.update({name: dict()})
def add_rating(rating):
        if rating not in movies.keys():
                print("Thise movie doesn't exist ")
        else:
                user = input('Put name')
                rate = int(input('Enter your marks'))
                if user in list(movies[rating].keys()):
                        print('Name users repeat!!!')
                elif rate > 10 or rate <0:
                        print('Rating must be 0-10')
                else:
                        movies[rating].update({user: rate})
                        print('A rating passed')
def show_view():
    for c, d in movies.items():
        rating = []
        for i in d.values():
           rating.append(i)
        if len(rating) == 0:
            print(f"{c}havent rating")
        else:
            print(f"{c} is rate {sum(rating)/len(rating)}")

def show():
    for k, v  in movies.items():
        print(k, v)
while True:
    show()
    command = input('0) Close kode \n '
                    '1) Add Movie \n'
                    '2)Add rate\n '
                    '3) Show rates \n'
                    ' Put your command')
    if command == '1':
        movie_name = input('Name film').title()
        add_movies(movie_name)
    elif command == "2":
        movies_name = input('name film').title()
        add_rating(movies_name)
    elif command =="3":
        show_view()
    elif command == "0":
        print('Exit')
        break
    else:
        print('Command not found')
