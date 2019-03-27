def pierwsza(n):
    czy_pierwsza = True
    if n == 1:
        czy_pierwsza = False
    for i in range(n//2,1,-1):
        if n % i == 0:
            czy_pierwsza = False
    return czy_pierwsza


liczby_pierwsze = 0
najwieksza_pierwsza = 100
najmniejsza_pierwsza = 100
liczba_a = 0
liczba_b = 0
pary = []
with open("dane6.txt","r") as plik:
    for liczba in plik:
        liczba = liczba.strip()
        liczba = int(liczba)
        if pierwsza(liczba):
            liczby_pierwsze += 1
            liczba_a = liczba_b
            liczba_b = liczba
            if abs(liczba_a - liczba_b) == 2:
                pary.append(liczba_a)
                pary.append(liczba_b)
        if pierwsza(liczba):
            if liczba > najwieksza_pierwsza:
                najwieksza_pierwsza = liczba
            if liczba < najmniejsza_pierwsza:
                najmniejsza_pierwsza = liczba
with open("wyniki6_3.txt","w") as wyniki:
    for i in range(0,8,2):
            wyniki.write(str(pary[i])+" ; "+str(pary[i+1])+"\n")
            
