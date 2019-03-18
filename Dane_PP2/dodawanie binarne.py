"""
Sumowanie binarne liczb
(C) Karolina Dudkowska
LO w Sobolewie, luty 2019r.
"""
def suma2(L1, L2):
    dalej = 0
    w = ''
    L1 = L1[::-1]
    L2 = L2[::-1]
    i = 0
    while len(L1)<len(L2):
    for z1 in L1:
        z1 = int(z1)
        z2 = int(L2[i])
        i += 1

