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
        sCyfr = dalej + int(L1[i]) + int(L2[i])
        if sCyfr>1:
            dalej = 1
        else:
            dalej = 0
        w = w + str(sCyfr%2)
    if dalej==1:
        w = w + '1'
    w = w[::-1]
    return w
print(suma2('101', '11101'))