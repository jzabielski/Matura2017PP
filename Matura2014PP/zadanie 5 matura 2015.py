"""
Zadanie 5 matura 2014 PP
(c)Mateusz Grzybowski , maj 2019
LO w Sobolewie
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

    return wzgl_p

with open("PARY_LICZB.TXT",'r') as plik:
    licznik_a = 0
    for i in plik:
        i = i.strip()
        liczba1, liczba2 = i.split(" ")
        liczba1 = int(liczba1)
        liczba2 = int(liczba2)
        print(f"{liczba1} - {liczba2}")
        if wielokrotne(liczba1, liczba2):
            licznik_a+=1
    with open("ZADANIE5.TXT", 'w') as w:
        w.write("a)\n"
                + str(licznik_a)
                + "\n")
        print(wzglednie_pierwsze(12, 11))
