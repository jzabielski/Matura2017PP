"""
Zadanie 5 matura 2015 PP
(C) Patryk Ragus, kwiecień 2019 r.
LO w Sobolewie
"""
N = []
slowa = []
nowe = []
for i in range(12):
    N.append(0)
with open("slowa.txt","r") as plik, open('nowe.txt','r') as plik2:
    for s in plik:
        s = s.strip()
        N[len(s)-1] += 1
        slowa.append(s)
    for n in plik2:
        n = n.strip()
        nowe.append(n)
with open('wynik5.txt','w+') as wynik:
    wynik.write("5.1\n")
    for i in range(12):
        wynik.write(str(i+1)+' '+str(N[i])+"\n")
    wynik.write("\n5.2\n")
    for n in nowe:
        wynik.write(n+' ')
        l_wyst = 0
        l_wyst_odbicia = 0
        for s in slowa:
            if n == s:
                l_wyst += 1
            if n[::-1] == s:
                l_wyst_odbicia += 1
        wynik.write(str(l_wyst) + ' ' + str(l_wyst_odbicia) + "\n")