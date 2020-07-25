import random

reci = open("Reci.txt", "r")
lista = []
for line in reci:
    red = line.strip()
    lista.append(red)
odgovor = True
ispis = []
def ponovo():
    pitanje = input("\nZelite li ponovo da igrate?\n")
    if(pitanje != "Da" and pitanje != "da" and pitanje != "Ne" and pitanje != "ne"):
        print("Unesite validan odgovor.")
        ponovo()
    elif(pitanje == "Da" or pitanje == "da"):
        vesalica()
        return True
    elif(pitanje == "Ne" or pitanje == "ne"):
        print("\nHvala vam i ocekujemo vas ponovo!")
        return False
def kalkulisanje(ispis, recList, rec, pokusaj, badCounter):
    goodCounter = 0
    for x in range(0, len(rec)):
        if(pokusaj == rec[x]):
            print("\nTacno!!!")
            goodCounter += 1
            for i in (0, len(ispis)):
                if(pokusaj == rec[x]):
                    ispis[x] = pokusaj
            for y in range(0, len(ispis)):
                print(ispis[y] + " ", end='')
    if(goodCounter == 0):
        badCounter += 1
        confirm = 5 - badCounter
        print("\nSlovo koje ste pokusali se ne nalazi u odabranoj reci. Gubite jedan pokusaj, " + str(5 - badCounter) + " ostalo.")
        if(confirm == 0):
            print("\nOstali ste bez dodatnih pokusaja. Rec je bila: " + rec + ".")
    if(ispis == recList):
        print("\nPogodili ste celu rec! Bravo!!!")
        return 11
    else:
        return badCounter
def vesalica():
    global ispis
    global lista
    rec = str(random.choice(lista))
    ispis = ["_"]*len(rec)
    recList = ["_"]*len(rec)
    for x in range(0, len(rec)):
        recList[x] = rec[x]
    badCounter = 0
    while(badCounter < 5 and badCounter != 11):
        izbor1 = input("\nZelite li da pogadjate: \n 1.Jedno slovo (Upisite 1)\n 2.Celu rec (Upisite 2) \n 3.Da izadjete iz programa upisite 0.\n")
        if(izbor1 != '1' and izbor1 != '2' and izbor1 != '0'):
            print("Odgovor nije validan.")
        elif(izbor1 == '1'):
            pokusaj = input("\nProbajte da pogodite koje se slovo nalazi u reci (Molimo koristite samo mala slova): ")
            badCounter = kalkulisanje(ispis, recList, rec, pokusaj, badCounter)
        elif(izbor1 == '2'):
            pokusaj = input("Unesite vas pokusaj reci (Molimo koristite samo mala slova): ")
            if(pokusaj == rec):
                print("Pogodili ste rec: " + rec)
                break
            elif(pokusaj != rec):
                badCounter += 1
                confirm = 5 - badCounter
                print("\nSlovo koje ste pokusali se ne nalazi u odabranoj reci. Gubite jedan pokusaj, " + str(5 - badCounter) + " ostalo.")
                if(confirm == 0):
                    print("\nOstali ste bez dodatnih pokusaja. Rec je bila: " + rec + ".")
                
        elif(izbor1 == '0'):
            break
vesalica()
while(odgovor == True):
    odgovor = ponovo()

