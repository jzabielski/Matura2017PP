"""
Matura 2016 PP Zadanie 1.4
(C) Cezary Winek
LO w Sobolewie, marzec 2019r.
"""

n = 123456
SumaCyfr = 0
while n>0:
    SumaCyfr = SumaCyfr + n%10
    n = n//10
print(SumaCyfr)