"""
Sumowanie binarne liczb
(C) Mateusz Grzybowski
LO w Sobolewie luty 2019r.
"""


def suma2(L1, L2):
    dalej = 0
    w = ''
    L1 = L1[::-1]
    L2 = L2[::-1]

    while len(L1) <= (L2):
        L2 =L2 + '0'

    for z1 in range(len(L1)):
        z1 = int(L1[i])
        z2 = nt(L2[i])
        scyfr = (dalej + z1 +z2)%2
        if scyfr>1
            dalej = 1

