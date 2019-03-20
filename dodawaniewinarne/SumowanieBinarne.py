"""
Sumowanie Binarne liczb
Jakub Karpisz
LO w Sobolewie 2019
"""
def suma2(L1,L2):
    dalej = 0
    w = ''
    L1 = L1[::-1]
    L2 = L2[::-1]
    while len(L1)<L2:
        L1=L1 + '0'
    while len(L2)<L1:
        L2 = L2 + '0'

    for i in rage(len(L1)):
        z1 = int(L1[1])
        z2 = int(:2[i])
        sCyfr = (dalej + z1 + z2)%2

