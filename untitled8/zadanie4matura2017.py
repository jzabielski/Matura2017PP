"""
Matura 2017 PP
Zadanie 4
(C) Izabela Lapacz
LO w Sobolewie, luty 2019r.
"""

rosnące = 0
with open("liczby.txt", "r") as plik:
    for liczby in plik:
        liczby = liczby.strip()
        L = liczby.split(" ")
        print(L[0],';', L[1], ";", L[2])
        if int(L[0]) < int(L[1]) and int(L[1]) < int(L[2]):
            rosnące += 1
with open("wyniki4.txt", "w") as odp:
    odp.write("4.1\n"+str(rosnące))