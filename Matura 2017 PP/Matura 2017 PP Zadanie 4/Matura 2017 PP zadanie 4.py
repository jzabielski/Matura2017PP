#Dawid Trojanowski
#LO Sobolew 2019
d = open('liczby.txt', 'r')
w = open('wyniki4.txt', 'r+')

licznik1 = 0
sumaD2 = 0

for i in range (1000):
    liczby = d.readline().strip()
    a, b, c = liczby.split()
    # 4.1
    a = int(a)
    b = int(b)
    c = int(c)
    if (a<=b) and (b<=c):
        licznik1 += 1
    #4.2
    Min = a
    if b < Min:
        Min = b
    if c < Min:
        Min = c
    j = Min
    NWD = 0
    while(NWD == 0):
        if (a%j==0) and (b%j==0) and (c%j==0):
            NWD = j
        else:
            j -= 1
    sumaD2 += NWD

#wydruki
print(licznik1)
print(sumaD2)
w.write("4.1\n")
w.write(str(licznik1)+"\n")
w.write("4.2\n")
w.write(str(sumaD2)+"\n")

d.close()
w.close()