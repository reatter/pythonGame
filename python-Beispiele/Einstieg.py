import os  # operating system

nummer = 2
zahl = 5
print("Hallo Paul, eine Zahl", zahl)


def schreibe(buchstaben=""):
    print(buchstaben)


schreibe(buchstaben="Hallo Paul")


def schreibe_in_datei(dateiname="/python/test/ausgabe.txt"):
    """schreibt sehr oft "Hallo Paul" in die ausgabe.txt-Datei
    """
    i = 17
    home_dir = os.environ['HOME']
    dateipfad = home_dir + dateiname
    datei_loeschen(dateipfad)
    schreibe_x_mal(x=i, dateipfad=dateipfad)


def schreibe_x_mal(x, dateipfad):
    i = 0
    with (open(file=dateipfad, mode="w") as file):
        while i < (x + 1):
            file.write("Hallo Paul " + str(i) + '\n')
            i = i + 1
        file.close()


def datei_loeschen(dateipfad):
    with (open(file=dateipfad, mode='w') as file):
        file.truncate(0)
        file.close()
        pass


schreibe_in_datei()  # startet die Funktion
