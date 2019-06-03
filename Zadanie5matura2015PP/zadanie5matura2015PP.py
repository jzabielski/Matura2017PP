"""
Zadanie 5 matura 2015 PP
(C) Damian Kopik,
LO w Sobolewie Kwiecień 2019
"""
N = []
S = []
NS = []
for i in range(12):
    N.append(0)
with open("slowa.txt", "r") as slowa:
    for s in slowa:
        s = s.strip()
        S.append(s)
        dl = len(s)
        N[dl - 1] += 1
with open("wynik5.txt", "w") as w:
    w.write("5.1\n")
    for i in range(12):
        w.write(str(i+1) + ", " + str(N[i]) + "\n")
    w.write("\n5.2\n")
    with open("nowe.txt", "r") as nowe_slowa:
        for ns in nowe_slowa:
            ns = ns.strip()
            NS.append(ns)
            licznik_ns = 0
            licznik_luster = 0
            ns_lustro = ns[::-1]
            for s in S:
                if s == ns:
                    licznik_ns += 1
                if s == ns_lustro:
                    licznik_luster += 1
            w.write(ns + " " + str(licznik_ns) + " " + str(licznik_luster) + "\n")
