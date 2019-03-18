"""
Zadanie 1.4 Matura 2016 PP
(C) Jakub Goliszewski, marzec 2019 r.
LO w Sobolewie
"""
n = 10
T = 'qqqwwweeee'
TS = ''
az = T[0]
i = 0
for z in T:
    if z == az:
        i += 1
    else:
        TS = TS + str(i) + az
        az = z
        i = 1
TS = TS + str(i) + z
print(TS)
print(len(TS))
