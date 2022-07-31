import random as rnd

vokale = ["a", 'i', 'e', 'u', 'o']
konsonanten = ['q', 'w', 'r', 't', 'y', 'i', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

def silbeGenerieren() :
    buchstabe1 = konsonanten[rnd.randint(0,21)]
    buchstabe2 = vokale[rnd.randint(0,4)]
    buchstabe3 = konsonanten[rnd.randint(0,21)]
    silbe = buchstabe1 + buchstabe2 + buchstabe3
    return silbe

case = rnd.randint(0,2)
Zahl = str(rnd.randint(0,9))

if case == 0:
    Passwort = [silbeGenerieren(), silbeGenerieren(), silbeGenerieren()]
    Passwort.insert(rnd.randint(0,3), Zahl)
elif case == 1:
    Passwort = [silbeGenerieren(), silbeGenerieren(), silbeGenerieren(), silbeGenerieren(), silbeGenerieren()]
    Passwort.insert(rnd.randint(0,5), Zahl)
elif case == 2:
    Zahl = Zahl + str(rnd.randint(0,9))
    Passwort = [silbeGenerieren(), silbeGenerieren(), silbeGenerieren(), silbeGenerieren(),silbeGenerieren(), silbeGenerieren()]
    Passwort.insert(rnd.randint(0,6), Zahl)

print(''.join(str(x) for x in Passwort))