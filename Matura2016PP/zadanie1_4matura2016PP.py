"""
Matura 2016 PP Zadanie 1.4
(C) Cezary Winek
LO w Sobolewie, marzec 2019r.
"""

n = 10
T = 'qqqwwwweeeeee'
# b = ? rozmiar skompresowanego tekstu
TS = ''
az = T[0]
i = 0
for z in T:
    if z == az:
        i+=1
    else:
        TS = TS + str(i) + az
        az = z
        i = 1
TS = TS + str(i) + az
print(TS)