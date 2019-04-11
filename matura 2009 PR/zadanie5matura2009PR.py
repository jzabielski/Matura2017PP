"""
Zadanie 5 matura 2009 PR
"""
def palindrom(s):
    pal = s == s[::-1]
    return pal

def sklejenie(A, B):
    wynik = B in A
    if not wynik:
        k = 0
        while A[-k-1]!=B[0]:
            k+=1


    return wynik

licznik_pal = 0
licznik_BwA = 0
licznik_par = 0
with open('dane.txt','r') as d:
    for slowa in d:
        slowa =  slowa.strip()
        slowa=slowa.split(" ")
        s1=slowa[0]
        s2=slowa[1]
        if palindrom(s1):
            licznik_pal += 1
        if palindrom(s2):
            licznik_pal += 1
        if s2 in s1:
            licznik_BwA += 1
        if not sklejenie(s1, s2):
            licznik_par +=1


with open('zad_5.txt', 'w') as w:
    w.write('a)\n'+str(licznik_pal)+'\n\n')
    w.write('b)\n' + str(licznik_BwA) + '\n\n')
    w.write('c)\n' + str(licznik_par) + '\n\n')
a='abcd'
print(a, a[:-2])