"""
Zadanie 5 matura 2015PP
(C) Karol Kożuchowski
LO w Sobolewie
"""

with open("slowa.txt",'r') as slowa:
    for s in slowa:
        s = s.strip()
        print(s)