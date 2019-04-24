# Zadanie 6 Matura 2016

# LO im. Tadeusza Kościuszki w Sobolewie

import math

def pierwsza(a):
    p = True
    i = 2
    while(p and i<=(a/2)):
        if(a%i==0):
            p = False
        i+=1

    return p

d = open("dane6.txt", "r")
w = open("wyniki6.txt", "w")
a = []
for i in range(2000):
    a.append(int(d.readline().strip()))
    print(a[i])
licznik1 = 0
MaxP = 0
# MinP = 30000
for i in range(2000):
    if(pierwsza(a[i])):
        licznik1+=1
        if(a[i]>MaxP):
            MaxP = a[i]
        # if (a[i] > MinP):
           # MinP = a[i]
print(licznik1)
w.write("6.1"+"\n")
w.write(str(licznik1)+"\n\n")
print(MaxP)
w.write("6.2"+"\n\n")
w.write(str(MaxP))
#6.3
licznikPar = 0
w.write("6.3"+"\n")
for i in range (1999):
    if (pierwsza(a[i]) and pierwsza(a[i+1])) and (math.fabs(a[i]-a[i+1]==2)):
        licznikPar+=1
        w.write(str(a[i]) + " - " + str(a[i+1]) + "\n")
w.write("liczba par bliźniaczych: " + str(licznikPar))

d.close()
w.close()