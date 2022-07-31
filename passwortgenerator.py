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
if case == 0:
    Zahl = str(rnd.randint(0,9))
    zahlPos = rnd.randint(0,3)
    if zahlPos == 0:
        Passwort = Zahl + silbeGenerieren() + silbeGenerieren() + silbeGenerieren()
    elif zahlPos == 1:
        Passwort =  silbeGenerieren() + Zahl + silbeGenerieren() + silbeGenerieren()
    elif zahlPos == 2:
        Passwort =  silbeGenerieren() + silbeGenerieren()+ Zahl + silbeGenerieren()
    elif zahlPos == 3:
        Passwort =  silbeGenerieren() + silbeGenerieren()+ silbeGenerieren() + Zahl
elif case == 1:
    Zahl = str(rnd.randint(0,9))
    zahlPos = rnd.randint(0,5)
    if zahlPos == 0:
        Passwort = Zahl + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren()
    elif zahlPos == 1:
        Passwort = silbeGenerieren() + Zahl + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren()
    elif zahlPos == 2:
        Passwort = silbeGenerieren() + silbeGenerieren() + Zahl + silbeGenerieren() + silbeGenerieren() + silbeGenerieren()
    elif zahlPos == 3:
        Passwort = silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + Zahl + silbeGenerieren() + silbeGenerieren()
    elif zahlPos == 4:
        Passwort = silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + Zahl + silbeGenerieren()
    elif zahlPos == 5:
        Passwort = silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + Zahl
elif case == 2:
    zahlPos = rnd.randint(0,6)
    Zahl = str(rnd.randint(0,9)) + str(rnd.randint(0,9))
    if zahlPos == 0:
        Passwort = Zahl + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren()
    elif zahlPos == 1:
        Passwort = silbeGenerieren() + Zahl + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() 
    elif zahlPos == 2:
        Passwort = silbeGenerieren() + silbeGenerieren() + Zahl + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren()
    elif zahlPos == 3:
        Passwort = silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + Zahl + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() 
    elif zahlPos == 4:
        Passwort = silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + Zahl + silbeGenerieren() + silbeGenerieren()
    elif zahlPos == 5:
        Passwort = silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + Zahl + silbeGenerieren()
    elif zahlPos == 6:
        Passwort = silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + silbeGenerieren() + Zahl
    
print(Passwort)