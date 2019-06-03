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

with open("PARY_LICZB.TXT",'r') as plik:
    for i in plik:
        i = i.strip()
        liczba1, liczba2 = i.split(" ")
        liczba1 = int(liczba1)
        liczba2 = int(liczba2)
        print(f"{liczba1} - {liczba2}")
print(wielokrotne(10,5))