# (C)Dawid Trojanowski
# Sumowanie Binarne Liczb
# Luty 2019
#(C) LO w Sobolewie 
def suma2(L1,L2):
	dalej = 0
	w = ''
	L1 = L1[::-1]
	L2 = L2[::-1]
	i = 0
	while len(L1) < len(L2):
		L1 = L1 + '0'
	while len(L2) < len(L1):
		L2 = L2 + '0 '
	for i in range(len(L1)):
		z1 = int(L1)
		z2 = int(L2[i])
		i += 1
		scyfr = (dalej + z1 + z2) % 2 
		if scyfr > 1:
			dalej = 1
		w = w + str(cyfr)
	w = w[::-1]