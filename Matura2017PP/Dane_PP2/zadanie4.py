def nwd(a,b,c):
    NWD = 1
    for i in range(max(a,b,c),1,-1):
        if a%i==0 and b%i==0 and c%i==0:
            NWD = i
            break
    return NWD

def suma(n):
    suma = 0
    for i in str(n):
        suma += int(i)
    return suma
print(suma(567))
