"""
Zadanie 6 matura 2016 PP
(C) Jarosław Zabielski, marzec 2019
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
    min1 = 30001
    max1 = 0
    pd = 4
    blizniacze = ""
    for d in plik:
        d = d.strip()
        d = int(d)
        if pierwsza(d):
            licznik1+=1
            if d<min1:
                min1 = d
            if d>max1:
                max1 = d
            if pierwsza(pd) and abs(d - pd)==2:
                blizniacze = blizniacze + str(pd)+ " " + str(d) + "\n"
        pd = d
with open("wyniki_6.txt", "w") as w:
    w.write("6.1\n"+str(licznik1)+"\n\n")
    w.write("6.2\n" + str(min1) + "\n"+ str(max1) + "\n\n")
    w.write("6.3\n" + blizniacze)
