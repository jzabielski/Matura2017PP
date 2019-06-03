"""
Zadanie 5 matura 2014 PP
(C) Jarosław Zabielski, maj 2019
LO im. T. KOściuszki w Sobolewie
"""
def wielokrotne(a, b):
    wiel = False
    if a!=0 and b!=0:
        if a%b == 0 or b%a == 0:
            wiel = True
    return wiel

def wzglednie_pierwsze(a, b):
    wzgl_p = True
    min_ab = min(a, b)
    for i in range(2, min_ab+1):
        if a%i == 0 and b%i == 0:
            wzgl_p = False
            break
    return wzgl_p

def suma_cyfr(a):
    suma = 0
    for c in str(a):
        suma += int(c)
    return suma

with open("PARY_LICZB.TXT",'r') as plik:
    licznik_a = 0
    licznik_b = 0
    licznik_c = 0
    for i in plik:
        i = i.strip()
        liczba1, liczba2 = i.split(" ")
        liczba1 = int(liczba1)
        liczba2 = int(liczba2)
        print(f"{liczba1} - {liczba2}")
        if wielokrotne(liczba1, liczba2):
            licznik_a += 1
        if wzglednie_pierwsze(liczba1, liczba2):
            licznik_b += 1
        if suma_cyfr(liczba1) == suma_cyfr(liczba2):
            licznik_c += 1
    with open("ZADANIE5.TXT", 'w') as w:
        w.write("a)\n"
                + str(licznik_a)
                + "\n")
        w.write("b)\n"
                + str(licznik_b)
                + "\n")
        w.write("c)\n"
                + str(licznik_c)
                + "\n")

print(licznik_a)
print(licznik_b)
print(licznik_c)