# 1 - Pravdivost tvrzení
x=int(input("Zadej hodnotu proměnné x\n"))
y=int(input("Zadej hodnotu proměnné y\n"))
if x+3<5*y-1:
    print(f"Vzorce x+3<5*y-1 je pravdivý")
else:
    print(f"Vzorce x+3<5*y-1 je nepravdivý")


# 2 - Dělení
x=int(input("Zadej hodnotu proměnné x\n"))
y=int(input("Zadej hodnotu proměnné y\n"))
if x%y==0:
    print("Číslo x je dělitelné číslem y beze zbytku")
else:
    print("Číslo x není dělitelné číslem y beze zbytku")



# 3 - Vypočtení zlomku
x=int(input("Zadej hodnotu proměnné x\n"))
y=int(input("Zadej hodnotu proměnné y\n"))
if x*y==0:
    print("Nulou nelze dělit")
else:
    print(f"Výsledek zlomku 1/({x}*{y}) je {1/(x*y)}")


# 4 - Porovnání čísel - min - max
cisla=int(input("Zadejte 3 celá čísla oddělená čárkou a mezerou\n"))
list_cisel=cisla.split(", ")
print(list_cisel)
print(min(list_cisel))
print(max(list_cisel))


# 4 - Porovnání čísel - min - max se smyckou for
cisla=input("Zadejte 3 celá čísla oddělená čárkou a mezerou\n")
list_cisel=cisla.split(", ")
print(list_cisel)
minimum=None
maximum=None
for x in list_cisel:
    if minimum is None or int(minimum)>int(x):
        minimum=x
    if maximum is None or int(maximum)<int(x):
        maximum=x
print(f"Minimální hodnota je {minimum} a maximální hodnota  je {maximum}")


# 5 - Porovnání výšky žáků
zak1=input("Zadej jméno žáka a jeho výšku  - oddělené čárkou a mezerou\n")
list_zak1=zak1.split(", ")
zak2=input("Zadej jméno žáka a jeho výšku  - oddělené čárkou a mezerou\n")
list_zak2=zak2.split(", ")
print(list_zak1)
print(list_zak2)
if int(list_zak1[1])>int(list_zak2[1]):
    print(f"Žák {list_zak1[0]} je vyšší než žák {list_zak2[0]}")
elif int(list_zak1[1])<int(list_zak2[1]):
    print(f"Žák {list_zak1[0]} je menší než žák {list_zak2[0]}")
else:
    print(f"Žáci{list_zak1[0]} a {list_zak2[0]} mají stejnou výšku")



# 6 - Porovnání rychlosti aut
s1=int(input("Zadejte délku trasy auta 1 v km\n"))
t1=int(input("Zadejte čas trasy auta 1 v min.\n"))
prumer1=t1/s1

s2=int(input("Zadejte délku trasy auta 2 v km\n"))
t2=int(input("Zadejte čas trasy auta 2 v min. \n"))
prumer2=t2/s2

if prumer1>prumer2:
    print("Auto 1 mělo vyšší průměrnou rychlost")
elif prumer1<prumer2:
    print("Auto 2 mělo vyšší průměrnou rychost")
else:
    print("Obě auta jely stejně rychle")



# 7 - Státní zřízení podle letopočtu
rok=int(input("Zadejte letopočet od roku 1600\n"))
zrizeni=["Rakousko-Uhersko", "Československá republika", "Protektorát Bohmen und Mahren", "Československá socialistická republika", "ČSFR", "Česká republika"]
if rok<1918:
    x=0
elif rok<1939:
    x=1
elif rok<1945:
    x=2
elif rok<1960:
    x=1
elif rok<1990:
    x=3
elif rok>=1993:
    x=4

print(f"Státní zřízení v roce {rok} bylo {zrizeni[x]}")
    



# 8 - Zjištění o jaký znak se jedná
retezec=input("Zadejte nějaký řetězec znaků, číslic nebo písmen\n")
velka_pismena=0
mala_pismena=0
znaky=0
cislice=0
for znak in retezec:
    if ord(znak) in range(65, 90):
        velka_pismena=velka_pismena+1
    elif ord(znak) in range(97, 122):
        mala_pismena=mala_pismena+1
    elif ord(znak) in range(48, 57):
        cislice=cislice+1
    else:
        znaky=znaky+1
   
print(f"Počet velkých písmen je {velka_pismena}, malých písmen {mala_pismena}, číslic {cislice} a znaků {znaky}")



# 9 - Porovnání čísel
x=input("Zadejte 1. číslo:\n")
y=input("Zadejte 2. číslo:\n")
if x>y:
    print ("1. číslo je větší než druhé")
elif x<y:
    print ("2. číslo je větší než první")
else:
    print ("Obě čísla jsou stejná")

# 10 - odmocnina
cislo=float(input("Zadejte číslo\n"))
if cislo<0:
    print("Toto číslo nebudu odmocňovat :-)")
else:
    print(f"Odmocnina čísla {cislo} je {cislo**(1/2)}")

# 11 - Čtverec nebo obdélník?
x=int(input("Zadejte stranu x:\n"))
y=int(input("Zadejte stranu y:\n"))
if x==y:
    print(f"Strana čtverce má délku {x} cm")
else:
    print(f"Strany obdélníků jsou {x} cm a {y} cm")


# 12 - program ze zeptá na denní dobu a teplotu
doba=input("Je den a/n\n").lower()
teplota=float(input("Zadej teplotu ve stupní Celsia:\n"))
if doba=="a" and teplota>=28:
    print("Doporučuji jít se dnes koupat - je opravdu teplo")
else:
    print("Čtení knížky doma může být fajn relaxace")



# 13 - program ukončení
otazka=input("Chcete skončit a/n\n").lower()
if otazka=="n":
    print("A stejně skončím")
    quit
    
else:
    quit



# -------------------------- SEKCE C ---------------------------------------
# 1 - genrování sinx
# import math
# for x in range (0,math.pi*2,0.1):
#     print(math.sin(x))


# 2 - Interval čísel - vylepšení o zadání rozsahu intervalu uživatelem
import random
cislo=0
cisla_v_intervalu=[]
random_cisla=[]
zadani=input("Zadejte rozmezí intervalu v celých číslech mezi 0 a 100 - čísla oddělte čárkou a mezerou\n")
interval=zadani.split(", ")
for x in range(10):
    cislo=random.randint(-90,100)
    random_cisla.append(cislo)
    if cislo>=int(interval[0]) and cislo<=int(interval[1]):
        cisla_v_intervalu.append(cislo)
print(f"Náhodně vygenerovaná čísla jsou tato: {random_cisla}")
print(f"Počet čísel v intervalu {interval} je {len(cisla_v_intervalu)} a jsou to tyto {cisla_v_intervalu}")


# 3 - Sportka - tažení 5ti čísel od 1 do 49
import random
tiket=[]
for x in range(0,5):
    tiket.append(random.randint(1,49))
print(f"Vaše náhodná čísla pro tiket jsou {tiket}")



# 4 - klesající posloupnost 8 až -8
for x in range(-8,9):
    print(x)

# 4b - klesající posloupnost 8 až -8 sudá číslo
for x in range(-8,9,2):
    print(x)

# 5 - generování náhodných čísle od 10 do 50  a zjištění odchylky od střední hodnoty
import random
soucet=0
for x in range(20):
    soucet=soucet + random.randint(10,50)
print(f"Průměr generovaných čísel je {soucet/20} a liší od od střední hodnoty o {round((soucet/20)-30,2)} ")


# 6 - program na výpis počtu a průměr žáků ve třídě
tridy=int(input("Zadejte počet tříd\n"))
zaci=0
soucet=0
for x in range(1,tridy+1):
    soucet=soucet+int(input(f"Zadejte počet žáku ve třídě {x}\n"))

print(f"celkový počet žáků je {soucet}, průměrný počet žáků na třídu je {soucet//tridy}")



# 7 - program na simulaci jak se bude měnit kurz CZK k EUR - nevím jak nastavit, aby random číslo nezahrnovalo 28 přesně
import random
pole=[]
for x in range (1,21):
    pole.append(round(random.uniform(26,27.9999999),2))
    if x%5==0:
        print(pole)
        pole.clear()


# 7b - program na výpis čísel s určitým zarovnáním - nevím jak to vypsat jinak než pomocí listu - jinak se to bude vypisovat pod sebou
pole=[]
for x in range (1,21):
    pole.append(x)
    if x%5==0:
        print(pole)
        pole.clear()
        


# 8 - program na součet čísel
cislo=int(input("Zadejte celé číslo větší než 0\n"))
soucet=cislo
pocet_kroku=0
for pocet_kroku in range(1,cislo):
    soucet=soucet+pocet_kroku

print(f"Výsledný součet jednotlivých čísel čísla {cislo} je {soucet}")




# 9 - program na vyhodnocení kolika čísly je číslo dělitelné 
cislo=int(input("Zadejte celé číslo větší než 2\n"))
delitel=0
pocet_delitelu=0
kroky=0

for delitel in range(2,cislo):
    if cislo%delitel==0:
        pocet_delitelu +=1

if pocet_delitelu ==0 or cislo==2:
    print(f"Jedná se o prvočíslo, které je dělitelné jen 1 a {cislo}")

else:
    print(f"Jedná se o číslo, které je dělitelné {pocet_delitelu} čísly beze zbytku - kromě 1 a {cislo}")
