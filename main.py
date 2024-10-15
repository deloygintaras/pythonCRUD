import datetime

orders = [
    [
        'Harry Potter and the Goblet of Fire',
        datetime.datetime(2024, 10, 1, 10, 24, 0),
        datetime.datetime(2024, 10, 1, 13, 1, 0)
     ],
    [
        'Harry Potter and the Chamber of Secrets',
        datetime.datetime(2024, 10, 1, 10, 24, 0),
        datetime.datetime(2024, 10, 1, 13, 18, 0)
     ],
    [
        'Harry Potter and the Prisoner of Azkaban',
        datetime.datetime(2024, 10, 1, 10, 24, 0),
        datetime.datetime(2024, 10, 1, 12, 49, 0)
    ]
]

def printInfo(film, num = 1):
    print("-----------------------------------------")
    print("1. Sąrašas 2. Įdėti 3. Redaguoti 4. Trinti 5. Baigti programą")
    print("1. Filmų seansų atvaizdavimas")
    print("2. Naujo filmo seanso įkėlimas")
    print("3. Filmo seanso redagavimas")
    print("4. Filmo seanso šalinimas")
    print("5. Išeiti iš programos")
    print("-----------------------------------------")

def printFilm(film, num = 1):
    print(f"")

def printFilms():
    num = 1
    for film in films:
        printFilm(film, num)
        num += 1