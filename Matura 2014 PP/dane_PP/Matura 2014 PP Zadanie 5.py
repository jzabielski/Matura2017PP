# Matura 2014 PP, zadanie 5
# (C) Bartłomiej Bieńko
# wrzesień 2018
# LO im. Tadeusza Kościuszki w Sobolewie

def suma_cyfr(n):
    suma = 0
    m = n
    while m>0:
        suma = suma + m%10
        m = int(m/10)

pd = open("PARY_LICZB.TXT", 'r')
pw = open("ZADANIE5.TXT", 'w')
a = []
b = []
licznikw = 0
licznikwp = 0
liczniksumycyfr = 0
for i in range (1000):
    w = pd.readline().strip()
    a, b = w.split(" ")
    a = int(a)
    b = int(b)
    # a)
    if a<b:
        if b%a==0:
            licznikw+=1
    else:
        if a%b==0:
            licznikw+=1
    # b)
    if a<b:
        a,b = b,a # b jest mniejsze
    wpierw = True
    j = 2
    while wpierw and j<=b:
        if ((a%j)==0) and ((b%j)==0):
            wpierw = False
        j+=1
    if wpierw:
        licznikwp+=1
    # c)
    if (suma_cyfr(a)==suma_cyfr(b)):
        liczniksumycyfr+=1
print(suma_cyfr(12345))
pw.write("a) ")
pw.write(str(licznikw)+"\n\n")
pw.write("b) ")
pw.write(str(licznikwp)+"\n\n")
pw.write("c) ")
pw.write(str(liczniksumycyfr))
pd.close()
pw.close()