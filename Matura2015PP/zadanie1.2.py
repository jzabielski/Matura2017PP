d = 4
C = [0,0,0,1]

w = 0
mnoznik = 1
for i in range(0,d):
    w += C[i] * mnoznik
    mnoznik *= 6
print(w)
