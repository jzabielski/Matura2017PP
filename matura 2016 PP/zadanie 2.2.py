"""
(C) Jakub Goliszewski
Program obliczajacy sume cyfr
"""

n = 1234
sumaCyfr = 0
while n > 0:
    sumaCyfr += n % 10
    n = n//10
print(sumaCyfr)
