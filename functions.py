from os import system
import time
import random

#Konstansok
file = 'words.csv'
BOLDend = "\033[0;0m"
BOLDstart = "\033[1m"
betuk = ['a' ,'á' ,'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ö', 'ő', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ü', 'ű', 'v', 'w', 'x', 'y', 'z',]
szavak = []
temakorok = []
tippek = []
nehezseg = 1

érmék = 1
megnyert = []
elvesztett = []

def BeolvasasSzavak():
    with open('words.csv', 'r', encoding='utf-8') as forras:
        for row in forras:
            halmaz = row.split(';')
            szavak.append(halmaz[0])
            temakorok.append(halmaz[1])
            tippek.append(halmaz[2].strip())

def MentesSzavak():
    with open(file, 'w', encoding='utf-8') as cel:
        for i in range(len(szavak)):
            cel.write(f'{szavak[i]};{temakorok[i]};{tippek[i]}\n')
    szavak.clear()
    temakorok.clear()
    tippek.clear()

def BolvasasStat():
    with open('playerdata.csv', 'r', encoding='utf-8') as forras:
            global érmék
            global elvesztett
            global megnyert
            érmék = int(forras.readline().strip())
            for i,row in enumerate(forras):
                halmaz = row.strip().split(';')
                if i == 0:
                    megnyert.append(int(halmaz[0]))
                    elvesztett.append(int(halmaz[1]))
                if i == 1:
                    megnyert.append(int(halmaz[0]))
                    elvesztett.append(int(halmaz[1]))
                if i == 2:
                    megnyert.append(int(halmaz[0]))
                    elvesztett.append(int(halmaz[1]))

def MentesStat():
    with open('playerdata.csv','w',encoding='utf-8')as cel:
        cel.write(f'{érmék}\n')
        for i in range(3):
            cel.write(f'{megnyert[i]};{elvesztett[i]}\n')
    megnyert.clear()
    elvesztett.clear()

def Cimsor(hosszusag,cim):
    kotojel = '-'
    if nehezseg == 1:
        nehezszoval = '              Könnyű'
    if nehezseg == 2:
        nehezszoval = '             Közepes'
    if nehezseg == 3:
        nehezszoval = '               Nehéz'
    if érmék < 10:
        alcím2 = f'Érmék:0{str(érmék)}{nehezszoval}'
    if érmék >= 10:
        alcím2 = f'Érmék:{str(érmék)}{nehezszoval}'
    return BOLDstart + '<' + hosszusag * kotojel + ' ' + cim + ' ' + hosszusag * kotojel + '>' + '\n' + alcím2 + BOLDend +'\n\n'

def menu():
    system('cls')
    print(Cimsor(10,'Menü'))
    print(f'Kilépés\t\t\t(0)\nÚj játék\t\t(1)\nNehézség módosítása\t(2)\nSzavak módosítása\t(3)\nStatisztikák\t\t(4)\n')
    valasz = input(f'Válasz: ')
    return valasz

def Kilepes():
    system('cls')
    print('Kilépés.')
    time.sleep(0.5)
    system('cls')
    print('Kilépés..')
    time.sleep(0.5)
    system('cls')
    print('Kilépés...')
    time.sleep(0.5)
    system('cls')

def UjJatek():
    system('cls')
    #konstansok
    global elvesztett
    global megnyert
    global érmék
    segedszavak = ['help']
    lose = False
    elerhetobetuk = ['a' ,'á' ,'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ö', 'ő', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ü', 'ű', 'v', 'w', 'x', 'y', 'z',]
    hiba = 0
    jelenlegiszo = random.randint(0,len(szavak)-1)
    kitalalt = [' ',]
    helyesvalasz = False

    #játéloop
    while helyesvalasz != True:

        #Játék elemek
        system('cls')
        print(f'Témakör: {temakorok[jelenlegiszo].capitalize()}')
        Szo(kitalalt, szavak[jelenlegiszo])
        Hangman(hiba)
        Betuk(elerhetobetuk)

        valasztottbetu = input('A kilépéshez írja be "ESC", a segítséghez "HELP"\nVálassz egy betűt: ').lower()

        #Feladás
        if valasztottbetu.lower() == 'esc':
            valasz = False
            while valasz != True:
                system('cls')
                print('Biztos fel szeretné adni? (i/n)')
                valasztas = input('Válasz: ')
                if valasztas.lower() == 'i':
                    valasz = True
                    if nehezseg == 1:
                        hiba = 10
                    if nehezseg == 2:
                        hiba = 5
                    if nehezseg == 3:
                        hiba = 3
                elif valasztas.lower() == 'n':
                    valasz = True
                else:
                    system('cls')
                    print('Hibás válasz!')
                    time.sleep(1.5)
        #Segítség felajánlása
        if valasztottbetu.lower() in segedszavak:
            segitseg = Segitseg(jelenlegiszo,elerhetobetuk)
            if not segitseg == None: 
                valasztottbetu = segitseg
                system('cls')
        #Ellenőrzés
        if valasztottbetu.lower() not in elerhetobetuk:
            if valasztottbetu.lower() not in segedszavak:
                if not valasztottbetu.lower() == 'esc':
                    system('cls')
                    print('Olyan betűt adjon meg, amit még nem használt fel!')
                    time.sleep(1.5)
                    system('cls')
        else:
            if not valasztottbetu in szavak[jelenlegiszo].lower():
                hiba = hiba + 1
                for i,egybetu in enumerate(elerhetobetuk):
                            if valasztottbetu == egybetu:
                                elerhetobetuk.pop(i)
                print(f'A(z) "{valasztottbetu}" betű nincs a szóban.')
                time.sleep(1)
            else:
                for i,betu in enumerate(szavak[jelenlegiszo]):
                    if betu == valasztottbetu:
                        kitalalt.append(i)
                        for i,egybetu in enumerate(elerhetobetuk):
                            if valasztottbetu == egybetu:
                                elerhetobetuk.pop(i)
                print(f'A(z) "{valasztottbetu}" betű megtalálható a szóban.')
                time.sleep(1)

        #nyerés ellenőrzés
        if len(kitalalt) == len(szavak[jelenlegiszo])+1:
            system('cls')
            print(f'A keresett szó: {szavak[jelenlegiszo].capitalize()}\nGratulálok, győztél\n')
            helyesvalasz = True
            if nehezseg == 1:
                érmék = érmék + 1
                megnyert[0] += 1
                print('+1 érme')
            if nehezseg == 2:
                érmék = érmék + 3
                megnyert[1] += 1
                print('+3 érme')
            if nehezseg == 3:
                érmék = érmék +5
                megnyert[2] += 1
                print('+4 érme')
            time.sleep(2.2)

        #vesztés ellenőrzés
        if nehezseg == 1:
            if hiba > 9:
                lose = True
                elvesztett[0] += 1
        if nehezseg == 2:
            if hiba > 4:
                lose = True
                elvesztett[1] += 1
        if nehezseg == 3:
            if hiba > 2:
                lose = True
                elvesztett[2] += 1
        if lose == True:
            system('cls')
            print(f'A keresett szó: {szavak[jelenlegiszo].capitalize()}\nVesztettél\n')
            print('  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n\n')
            helyesvalasz = True
            time.sleep(2.2)

def Szo(kiirando, jelenlegiszo):
    listaszo = []
    for betu in jelenlegiszo:
        listaszo.append(betu)
    for i, betu in enumerate(jelenlegiszo):
        if not i in kiirando:
            if not betu == ' ':
                listaszo[i] = '_'
    vegleges = "".join(listaszo)
    print(vegleges.capitalize())

def Betuk(elerhetobetuk):
    text = ''
    for betu in elerhetobetuk:
        text = text + f' {betu}'
    print(f'Elérhető betűk:{text.upper()}')

def Hangman(hiba):
    if hiba == 0:
        print('\n\n\n\n\n\n\n\n')
    if nehezseg == 1:
        if hiba == 1:
            print('       \n       \n       \n       \n       \n       \n=========\n')
        if hiba == 2:
            print('      |\n      |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 3:
            print('  _____\n      |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 4:
            print('  _____\n  |   |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 5:
            print('  _____\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n')
        if hiba == 6:
            print('  _____\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========\n')
        if hiba == 7:
            print('  _____\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========\n')
        if hiba == 8:
            print('  _____\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========\n')
        if hiba == 9:
            print('  _____\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========\n')
        if hiba == 10:
            print('  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n')
    if nehezseg == 2:
        if hiba == 1:
            print('       \n       \n       \n       \n       \n       \n=========\n')
        if hiba == 2:
            print('      |\n      |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 3:
            print('  _____\n      |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 4:
            print('  _____\n  |   |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 5:
            print('  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n')
    if nehezseg == 3:
        if hiba == 1:
            print('       \n       \n       \n       \n       \n       \n=========\n')
        if hiba == 2:
            print('  _____\n  |   |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 3:
            print('  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n')

def Nehezseg():
    loop = False
    global nehezseg
    while loop != True:
        system('cls')
        if nehezseg == 1:
            nehezszoval = 'Könnyű'
        if nehezseg == 2:
            nehezszoval = 'Közepes'
        if nehezseg == 3:
            nehezszoval = 'Nehéz'
        print(f'A játék nehézségének módosítása\nJelenlegi nehézség:{nehezszoval}\n\nKönnyű\t10 próbálkozás \t(1)\nKözepes\t5 próbálkozás\t(2)\nNehéz\t3 próbálkozás\t(3)\n')
        valasz = input(f'Válasz: ')
        if valasz == '1':
            system('cls')
            loop = True
            print('Nehézség beállítva a következőre: Könnyű')
            time.sleep(1.5)
            nehezseg = int(valasz)
        elif valasz == '2':
            system('cls')
            loop = True
            print('Nehézség beállítva a következőre: Közepes')
            time.sleep(1.5)
            nehezseg = int(valasz)
        elif valasz == '3':
            system('cls')
            loop = True
            print('Nehézség beállítva a következőre: Nehéz')
            time.sleep(1.5)
            nehezseg = int(valasz)
        else:
            system('cls')
            print('Hibás válasz')
            time.sleep(1.5)

def Szavak():
    valasz = ''
    while valasz != '0':
        system('cls')
        print('Vissza a főmenübe\t(0)\nSzavak kilistázása\t(1)\nSzó törlése\t\t(2)\nSzó hozzáadása\t\t(3)\n')
        valasz = input('Válasz: ')
        if valasz == '0':
            Kilepes()
        elif valasz == '1':
            Osszesszo()
        elif valasz == '2':
            Szotorles()
        elif valasz == '3':
            Szohozzaad()
        else:
            system('cls')
            print('Hibás válasz!')
            time.sleep(1.5)

def Szotorles():
    valasz = False
    while valasz != True:
        system('cls')
        bekertszo = input('Adja meg a törölni kívánt szót: ')
        if not bekertszo.lower() in szavak:
            print('Ilyen szó nem létezik.')
            time.sleep(1.5)
        else:
            for i,szo in enumerate(szavak):
                if bekertszo.lower() == szo:
                    szavak.pop(i)
                    temakorok.pop(i)
                    tippek.pop(i)
            print(f'\nA(z) {bekertszo.capitalize()} törölve.')
            valasz = True
            time.sleep(1.5)

def Osszesszo():
    system('cls')
    for szo in szavak:
        print('\t',szo.capitalize())
    input('\nA továbblépéshez nyomja meg az ENTER billlenytűt!')

def Szohozzaad():
    system('cls')
    szavak.append(input('Adjon meg egy szót: ').lower())
    temakorok.append(input('Adja meg a szó témakörét: ').lower())
    tippek.append(input('Adjon a szóhoz tippet: ').capitalize())

def Segitseg(jelenlegiszo, elerhetobetuk):
    global érmék
    halmaz1 = set(szavak[jelenlegiszo])
    halmaz2 = set(elerhetobetuk)
    metszet = halmaz1 & halmaz2
    if érmék < 10:
        alcím3 = f'Érmék:0{str(érmék)}'
    else:
        alcím3 = f'Érmék:{str(érmék)}'
    valasztas = False
    while valasztas != True:
        system('cls')
        print(f'{BOLDstart}Segítség vásárlás   {alcím3}{BOLDend}\n')
        print(f'Mégse\t\t\t(0)\nBetű tipp    1 érme\t(1)\nDefiníció    5 érme\t(2)')
        valasz = input('\nVálasz: ')
        if valasz == '0':
            Kilepes()
            valasztas = True
        elif valasz == '1':
            if érmék < 1:
                system('cls')
                print('Nincs elegendő érméd.')
                time.sleep(1.5)
            else:
                valasztas = True
                érmék = érmék -1
                return list(metszet)[random.randint(0,len(list(metszet))-1)]
        elif valasz == '2':
            if érmék < 5:
                system('cls')
                print('Nincs elegendő érméd.')
                time.sleep(1.5)
            else:
                system('cls')
                print(f'{tippek[jelenlegiszo]}')
                time.sleep(3)
                érmék = érmék -5
                valasztas = True
        else:
            system('cls')
            print('Hibás válasz!')
            time.sleep(1.5)

def Statisztikak():
    system('cls')
    osszeg = []
    szazalek = []
    for i in range(3):
        osszeg.append(int(megnyert[i]) + int(elvesztett[i]))
        if osszeg[i] == 0:
            szazalek.append(0)
        else:
            szazalek.append(int(megnyert[i])/(osszeg[i]/100))
    if sum(osszeg) == 0:
        osszszazalek = 0
    else:
        osszegszazalek = sum(megnyert)/(sum(osszeg)/100)
    print(f'{BOLDstart}Nehézség      Megnyert      Elvesztett      Nyerési Arány      Összes lejátszott{BOLDend}')
    print(f'Könnyű\t\t {megnyert[0]}\t\t{elvesztett[0]}\t\t{round(szazalek[0])}%\t\t\t{osszeg[0]}')
    print(f'Közepes\t\t {megnyert[1]}\t\t{elvesztett[1]}\t\t{round(szazalek[1])}%\t\t\t{osszeg[1]}')
    print(f'Nehéz\t\t {megnyert[2]}\t\t{elvesztett[2]}\t\t{round(szazalek[2])}%\t\t\t{osszeg[2]}')
    print(f'Összes\t\t {sum(megnyert)}\t\t{sum(elvesztett)}\t\t{round(osszegszazalek)}%\t\t\t{sum(osszeg)}')
    input('\nA továbblépéshez nyomja meg az "ENTER"-t')