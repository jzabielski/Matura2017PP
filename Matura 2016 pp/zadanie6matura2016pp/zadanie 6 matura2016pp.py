"""
Zadanie 6 matura 2016 PP
(C)
LO w Sobolewie
"""

import math as m
def pierwsza(n):
    czy_pierwsza = True
    for i in range(2, int(m.sqrt(n))+1, 1):
        if n%i == 0:
            czy_pierwsza = False
    return czy_pierwsza


with open("dane6.txt", "r") as plik:
    licznik1 = 0
    for d in plik:
        d = d.strip()
        d = int(d)
        if pierwsza(d):
            licznik1+=1
        print(d)
with open("wyniki_6.txt", "w") as w:
    w.write("6.1\n"+str(licznik1)+"\n")