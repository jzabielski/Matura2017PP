"""
Sumowanie binarne liczb
(C) Jarosław Zabielski
LO w Sobolewie, luty 2019 r.
"""
def suma2(L1, L2):
    dalej = 0
    w = ''
    L1 = L1[::-1]
    L2 = L2[::-1]
    while len(L1)<len(L2):
        L1 = L1 + '0'
    while len(L2)<len(L1):
        L2 = L2 + '0'
    for i in range(len(L1)):
        z1 = int(L1[i])
        z2 = int(L2[i])
        sCyfr = (dalej + z1 + z2)%2
        if sCyfr>1:
            dalej = 1
        w = w + str(sCyfr)
    w = w[::-1]
    return w
print(suma2('101', '11101'))