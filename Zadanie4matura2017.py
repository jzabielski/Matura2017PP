"""
Matura 2017 PP
Zadanie 4
(C) Jarosław Zabielski
LO w Sobolewie, luty 2018 r.
"""

def nwd(a, b, c):
    NWD = 1
    for i in range(max(a, b, c), 1, -1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            NWD = i
            break
    return NWD

def sumaCyfr(n):
    suma = 0
    while n>0:
        suma += n%10
        n = n//10
    return suma

rosnące = 0
sumaNWD = 0
sCyfr35 = 0
maxSCyfr = 0
ileMaxSCyfr = 0
with open("liczby.txt","r") as plik:
    for liczby in plik:
        liczby = liczby.strip()
        L = liczby.split(" ")
        print(L[0],';',L[1],";",L[2])
        L[0] = int(L[0])
        L[1] = int(L[1])
        L[2] = int(L[2])
        if L[0] < L[1] and L[1] < L[2]:
            rosnące += 1
        sumaNWD += nwd(L[0], L[1], L[2])
        sCyfrW = sumaCyfr(L[0]) + sumaCyfr(L[1]) + sumaCyfr(L[2])
        if sCyfrW == 35:
            sCyfr35 += 1
        if sCyfrW > maxSCyfr:
            maxSCyfr = sCyfrW
            ileMaxSCyfr = 1
        elif sCyfrW == maxSCyfr:
            ileMaxSCyfr += 1

with open("wyniki4.txt","w") as odp:
    odp.write("4.1\n"+str(rosnące)+"\n")
    odp.write("4.2\n" + str(sumaNWD) + "\n")
    odp.write("4.3\n" + str(sCyfr35) + "\n")
    odp.write(str(maxSCyfr) + "\n")
    odp.write(str(ileMaxSCyfr) + "\n")
