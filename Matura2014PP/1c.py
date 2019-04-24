n = int(input("Podaj liczbe = "))

d = 1
w = 1
while d<n:
    if n % d == 0:
        w *= d
    d += 1
if w == d:
    print("TAK")
else:
    print("NIE")
