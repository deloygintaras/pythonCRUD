import datetime
import csv

# films = [
#     ['Harry Potter and the Goblet of Fire',
#      datetime.datetime(2024, 10, 1, 10, 24, 0),
#      datetime.datetime(2024, 10, 1, 13, 1, 0), 12],
#
#
#     ['Wolfs',
#      datetime.datetime(2024, 10, 1, 10, 24, 0),
#      datetime.datetime(2024, 10, 1, 13, 18, 0), 10],
#
#
#     ['Lonely Planet',
#      datetime.datetime(2024, 10, 1, 10, 24, 0),
#      datetime.datetime(2024, 10, 1, 12, 49, 0), 9]
# ]

FILE_PATH = "films.csv"

def loadFilms():
    films = []
    with open(FILE_PATH, mode = 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            film = [
                row[0],
                datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S"),
                datetime.datetime.strptime(row[2],"%Y-%m-%d %H:%M:%S" ),
                row[3]
            ]
            films.append(film)
        return films

films = loadFilms()

def saveFilms(film):
    with open (FILE_PATH, mode = 'w', newline="") as file:
        writer = csv.writer(file)
        for film in films:
            writer.writerow([film[0], film[1].strftime("%Y-%m-%d %H:%M:%S"), film[2].strftime("%Y-%m-%d %H:%M:%S"), film[3]])

def printInfo():
    print("-----------------------------------------")
    print("1. Filmų seansų atvaizdavimas")
    print("2. Naujo filmo seanso įkėlimas")
    print("3. Filmo seanso redagavimas")
    print("4. Filmo seanso šalinimas")
    print("5. Filtruoti filmus")
    print("6. Išeiti iš programos")
    print("-----------------------------------------")

def printFilm(film, num):
    duration = film[2] - film[1]
    hours, remainder = divmod(duration.seconds, 3600)
    minutes = remainder // 60
    print(f"{num}. Seanso pavadinimas: {film[0]}. Seanso pradžia: {film[1]}. Seanso pabaiga: {film[2]}. Seanso trukmė: {hours} val. {minutes} min. Kaina: {film[3]} Eur")

def printFilms(film_list):
    for num, film in enumerate(film_list, start=1):
        printFilm(film, num)


def addFilm():
    filmTitle = input("Koks filmo pavadinimas? ")
    filmBeggins = datetime.datetime.strptime(input("Seanso pradžia (yyyy-mm-dd hh:mm:ss)? "), "%Y-%m-%d %H:%M:%S")
    filmEnd = datetime.datetime.strptime(input("Seanso pabaiga (yyyy-mm-dd hh:mm:ss)? "), "%Y-%m-%d %H:%M:%S")
    price = float(input("Kokia filmo kaina (Eur)? "))
    films.append([filmTitle, filmBeggins, filmEnd, price])
    saveFilms(films)

def editFilm():
    ed = int(input("Įveskite seanso numerį, kurį norite redaguoti: "))
    printFilm(films[ed - 1], ed)
    print("Suveskite naujas reikšmes:")
    filmTitle = input("Koks filmo pavadinimas? ")
    filmBeggins = datetime.datetime.strptime(input("Seanso pradžia (yyyy-mm-dd hh:mm:ss)? "), "%Y-%m-%d %H:%M:%S")
    filmEnd = datetime.datetime.strptime(input("Seanso pabaiga (yyyy-mm-dd hh:mm:ss)? "), "%Y-%m-%d %H:%M:%S")
    price = float(input("Kokia filmo kaina (Eur)? "))
    films[ed - 1] = [filmTitle, filmBeggins, filmEnd, price]

def removeFilm():
    rem = int(input("Įveskite seanso numerį kurį norite pašalinti: "))
    films.pop(rem - 1)

def filterByDuration():
    duration = int(input("Įveskite maksimalų filmų trukmę (minutėmis): "))
    filtered_films = [film for film in films if (film[2] - film[1]).seconds // 60 <= duration]
    printFilms(filtered_films)

def filterByTitle():
    title = input("Įveskite filmo pavadinimą (ar dalį pavadinimo): ").lower()
    filtered_films = [film for film in films if title in film[0].lower()]
    printFilms(filtered_films)

def filterByPrice():
    max_price = float(input("Įveskite maksimalą kainą (Eur): "))
    filtered_films = [film for film in films if film[3] <= max_price]
    printFilms(filtered_films)

print("--- FILMŲ SEANSŲ VALDYMO SISTEMA ---")

while True:
    printInfo()
    opt = int(input())
    match opt:
        case 1:
            printFilms(films)
        case 2:
            addFilm()
            printFilms(films)
        case 3:
            editFilm()
            printFilms(films)
        case 4:
            removeFilm()
            printFilms(films)
        case 5:
            print("1. Filtruoti pagal trukmę")
            print("2. Filtruoti pagal pavadinimą")
            print("3. Filtruoti pagal kainą")
            filter_opt = int(input("Pasirinkite filtravimo variantą: "))
            match filter_opt:
                case 1:
                    filterByDuration()
                case 2:
                    filterByTitle()
                case 3:
                    filterByPrice()
        case 6:
            print("Išeinama iš programos.")
            exit(1)

