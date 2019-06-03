"""
zadanie 5 matura 2018 PP
(C)Jarosław Zabielski
LO w Sobolewie, styczeń 2019 r.
"""
def sumaCyfr1(n):   # n - całkowite
    suma = 0
    for i in str(n):
        suma +=int(i)
    return suma

def sumaCyfr2(n):   # n - string
    suma = 0
    for i in n:
        suma += int(i)
    return suma


with open("liczby.txt",'r') as d:
    w = open("wyniki5.txt",'w')
    w.write('5.2\n')
    max = 0
    for L in d:
        n = int(L.strip())
        m = L.strip()
        mOdwrotna = m[::-1]
        if m==mOdwrotna:
            w.write(m+'\n')
        if (n>max) and (n%2==0):
            max = n
    w.write("\n5.1\n"+str(max))

w.write("\n5.3\n")
with open("liczby.txt", 'r') as d:
    suma = 0
    for liczba in d:
        liczba = liczba.strip()
        suma_cyfr = sumaCyfr1(liczba)
        suma += suma_cyfr
        if suma_cyfr > 30:
            w.write(liczba+"\n")
    w.write("Suma wszystkich cyfr: "+str(suma))