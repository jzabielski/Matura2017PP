#Dawid Trojanowski
#LO Sobolew 2019

def palindrom(a):
    pal = True
    dl = len(a)
    for i in range(int(dl/2)):
        if(a[i]!=a[dl-1-i]):
            pal = False
    return pal

d = open ("liczby.txt", "r")
w = open ("wyniki5.txt", "w")
a = []
MaxParzysta = 0
for i in range(1000):
    a.append(int(d.readline().strip()))
    # print(a[i])
    if(a[i]%2==0 and a[i]>MaxParzysta):
        MaxParzysta = a[i]

w.write("5.1" + "\n" + str(MaxParzysta) + "\n\n")

#5.2
w.write("5.2" + "\n" + str(MaxParzysta) + "\n\n")
for i in range(1000):
    if(palindrom(str(a[i]))):
        w.write(str(a[i]) + "\n")
        print(a[i])

d.close()
w.close()