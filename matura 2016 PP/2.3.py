def suma_cyfr(n): 
    s = 0
    k = 10
    while n > 0:
            s += n % 10
            n = n//10
    return s
n = 375
k = 0
k = (n - suma_cyfr(n)) / 9
print(k)
