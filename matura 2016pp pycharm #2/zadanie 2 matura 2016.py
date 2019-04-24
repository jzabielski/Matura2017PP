"""
zadanie 2 matura 2016 PP
(C) Damian Pracz, marzec
LO w Sobolewie
"""

def suma_cyfr(n):
    n = 123456
    SumaCyfr = 0
    while n>0:
        SumaCyfr = SumaCyfr + n%10
        n = n//10
    return(SumaCyfr)
n = 123456
print(suma_cyfr(n))
k = (n - suma_cyfr(n)) /9
print(k)