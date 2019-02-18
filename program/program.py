rosnace = 0
with open('liczby.txt','r') as plik:
    for liczby in plik:
        liczby = liczby.strip()
        L = liczby.split(' ')
        print (L[1],';',L[1],";",L[2])
        if L[0] < L[1] and L[1] < L[2]:
            rosnace +=1
with open('wyniki3.txt','w') as odp:
    odp.write ("4.1\n"+str(rosnace)+'\n')

