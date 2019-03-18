"""
Zadanie 2 matura 2016 PP
(C) Jarosław Zabielski
LO w Sobolewie
"""
n = 123456
SumaCyfr = 0
while n>0:
    SumaCyfr = SumaCyfr + n%10
    n = n//10
print(SumaCyfr)