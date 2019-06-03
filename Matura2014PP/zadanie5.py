zad_a = 0
zad_b = 0
zad_c = 0
def wielokrotnosc(n1, n2):
	l1 = int(n1)
	l2 = int(n2)
	if l1 != 0 and l2 != 0:
		if l1 % l2 == 0 or l2 % l1 == 0:
			return True
		else:
			return False
	else:
		return False

def dzielnik(n1, n2):
	n2 = int(n2)
	n1 = int(n1)
	k = min(n1, n2)
	d = 0
	for i in range(k, 0, -1):
		if n1 % i == 0 and n2 % i == 0:
			d = i
			return d

def suma_cyfr(n):
	suma = 0
	for c in str(n):
		suma += int(c)
	return suma

with open("PARY_LICZB.txt", "r") as f:
	for line in f:
		line = line.strip()
		liczba1, liczba2 = line.split(" ")
		liczba1 = int(liczba1)
		liczba2 = int(liczba2)
		if wielokrotnosc(liczba1, liczba2):
			zad_a += 1
		if dzielnik(liczba1, liczba2) == 1:
			zad_b += 1
		if suma_cyfr(liczba1) == suma_cyfr(liczba2):
			zad_c += 1
print(zad_a)
print(zad_b)
print(zad_c)
with open("ZADANIE5.txt","w") as w:
	w.write("a)\n" + str(zad_a) + "\n")
	w.write("b)\n" + str(zad_b) + "\n")
	w.write("c)\n" + str(zad_c) + "\n")
