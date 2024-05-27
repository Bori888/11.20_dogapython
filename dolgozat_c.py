def feladat_1():
    print('Írjuk ki a számokat 120-tól 10-ig csökkenő sorrendben, 1 sorba 11 szám kerüljön! (3 pont)')
    for i in range (120, 9, -1):
        print(i, end=' ')
        if i % 11 == 0:
            print( end='\n')

def feladat_2():
    print('Kérj be addig tört számokat, amíg pozitív, kétjegyű (tört rész lehet mellette) nem lesz! (2 pont)')
    szam = float(input("Kérek egy pozitív, kétjegyű, tört számot: "))
    while not ((szam > 9) and (szam < 100)):
        szam = float(input("Kérek egy pozitív, kétjegyű, tört számot: "))

def feladat_3():
    print('Kérj be egy egész számot, majd írass ki a számtól kezdve páros számokat növekvő sorrendben, de csak 10 darabot, egymás mellé, szóközökkel elválasztva! (2 pont)')
    szam = int(input("Kérek egy egész számot: "))
    if szam % 2 == 0:
        for i in range(szam, szam +20, 2):
            print(i, end=' ')
    else:
        for i in range(szam+1, szam + 20, 2):
            print(i, end=' ')

def feladat_4():
    print('Kérj be 5 szót (csak ciklussal fogadom el), majd írasd ki a szavakat egymás mellé “*” jellel elválasztva! (pl. Be: “Ez”, “a”, “dolgozat”, “jól”, “sikerült.”, Ki: “Ez*a*dolgozat*jól*sikerült.” (2 pont)')
    szoveg = ''
    for i in range(1, 6, 1):
        szo = input("Kérek egy szót: ")
        szoveg += szo + "*"
    print(szoveg, end='')



