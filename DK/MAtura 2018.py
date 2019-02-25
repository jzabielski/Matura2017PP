"""
Matura 2017 PP
Zadanie 4
(C) Damian Kopik
LO SOBOLEW, luty 2019
"""
with open("liczby.txt","r") as plik:
    rosnace = 0 
    for liczby in plik:
        liczby = liczby.strip()
        L = liczby.split(" ")
    print(L[0],';',L[1],";",L[2])
    if L[0] < L[1] and L[1] < L[2]:
        rosnace += 1
with open("wyniki4.txt","w") as odp:
    odp.write("4.1\n"+str(rosnace))