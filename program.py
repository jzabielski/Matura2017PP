"""
Matura 2017 PP
Dawid Trojanowski
"""
rosnace = 0
with open('liczby.txt','r') as plik:
    for liczby in plik:
        liczby = (liczby.strip())
         liczba = liczby.spit('')
        print (L[1],';',liczba[1],";",L[2])
        if L[0] < L[1] and L[1] < L[2]:
            rosnace +=1
            print (rosnace)