movies = {
    "Django unchained": {
        "John": 10,
        "Jack": 9
    },

    "Troy": dict()
}


def find_movie(movie_name):
    if movie_name.capitalize() in movies.keys():
        return True


def add_movie(movie_name: str):
    if find_movie(movie_name.capitalize()):
        print('This film already exist!')
    else:
        movies[movie_name.capitalize()] = dict()
        print(f"'{movie_name.capitalize()}' added successfully\n")


def rate_movie(movie_name):
    if not find_movie(movie_name.capitalize()):
        print("This movie doesn't exist!")
    else:
        while 1:
            user = input('Enter your name: ').capitalize()
            if user in movies[movie_name.capitalize()].keys():
                print('This user already exist!')
                continue
            rate = int(input('Enter your rate: 1 - 10 '))
            if rate < 1 or rate > 10:
                print('Rate must be from 1 to 10')

            else:
                movies[movie_name.capitalize()][user] = rate
                print(
                    f'A rating has been added for {movie_name.capitalize()}:'
                    f' {user} rated it {rate}'
                )
                break


def all_movie_rates():
    for movie, rates in movies.items():
        if len(rates.values()) == 0:
            print(f'Rating is not yet available for {movie}')
        else:
            average = sum(rates.values()) / len(rates.values())
            print(f'{movie} is rated {round(average, 1)}')


while True:
    all_movie_rates()
    command = input(
        f'Choose the command:\n 1) Add movie\n 2) Rate to movie\n 0) Exit \n'
    )
    movie = input('Enter movie name: ')
    if command == '1':
        add_movie(movie)
    elif command == '2':
        rate_movie(movie)
    elif command == '0':
        print('Program stopped')
        break
