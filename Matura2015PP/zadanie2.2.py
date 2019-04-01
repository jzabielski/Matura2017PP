n = 3
k = 3
A = [1, 2, 3, 3, 2, 3, 3, 3]
T =[]
for i in range(k):
    T.append(0)
for c in A:
    T[c-1] += 1
y = 0
naj = 0
for i in range(k):
    print(T[i])
    if T[i] > naj:
        y = i

    

    
