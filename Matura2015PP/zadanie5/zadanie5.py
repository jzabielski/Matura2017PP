"""
Zadanie 5 matura 2015PP
(C) Jakub Goliszewski, kiecien 2019r.
LO Sobolew
"""
N = []
for i in range(12):
    N.append(0)
with open("slowa.txt","r") as plik:
    for slowo in plik:
        slowo = slowo.strip()
        N[len(slowo)-1] += 1
