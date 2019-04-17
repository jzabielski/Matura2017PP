"""
Zadanie 5 matura 2015 PP
(C) Patryk Ragus, kwiecień 2019 r.
LO w Sobolewie
"""
N = []
for i in range(12):
    N.append(0)
with open("slowa.txt", "r") as slowa:
    for s in slowa:
        s = s.strip()
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
            licznik_ns = 0
            for s in slowa:
                if s == ns:
                    licznik_ns += 1
            w.write(ns + " " + str(licznik_ns) + "\n")
