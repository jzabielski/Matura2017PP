#Dawid Trojanowski
#LO Sobolew 2019
dn = open("nowe.txt", 'r')
ds = open("slowa.txt", 'r')
w = open ("wynik5.txt", 'w')

s = []
n = []
MaxParzysta = 0
for i in range(1000):
    s.append(ds.readline().strip())
    print(i,s[i])

for i in range(25):
    n.append(dn.readline().strip())
    print(i,n[i])

#5.1
w.write("5.1"+"\n")
for i in range (1,13):
    licznik = 0
    for j in range(1000):
        if len(s[j])==i:
            licznik+=1
    print(i, ": ", licznik)
    w.write("5.1"+"\n")
    w.write(str(i) + ":" + str(licznik))
#5.2
w.wrie("5.2"+"\n")
for i in range(25):
    licznik1 = 0
    licznik2 = 0
    for j in range (1000):
        if n[i] == s[j]:
            licznik1+=1
        if lustro(n[i], s[j]):
            licznik2+=1
    print(n[i], ": ", licznik1, licznik 2)

dn.close()
ds.close()
w.close()