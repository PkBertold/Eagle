#Elkezdhetünk ebbe dolgozni
#Behívja az alakzatok számát, ki is számolja az eredményt, de amint beírom a printet, összeomlik, és csak az első sort számolja ki, szóval help


def haromszogKerulet():
	a=float(input("Kérem a háromszög egyik oldalát(kerület):"))
	b=float(input("Kérem a háromszög másik oldalát(kerület):"))
	c=float(input("Kérem a háromszög harmadik oldalát(kerület):"))
	return float((a+b+c))

def haromszogTerulet():
	a=float(input("Kérem a (nem derékszögű) háromszög egyik oldalát(terület):"))
	m=float(input("Kérem a (nem derékszögű) háromszög magasságát(terület):"))
	return float((a*m)/2)

def derekszoguharomszogTerulet():
	a=float(input("Kérem a derékszögű háromszög egyik oldalát(terület):"))
	b=float(input("Kérem a derékszögű háromszög másik oldalát(terület):"))
	return float((a*b)/2)

def korKerulet():
	r=float(input("Kérem adja meg kör sugarát:"))
	n=float(input("Kérem adja meg a kör n számát:"))
	return float(2*r*n)
	
def korTerulet():
	r=float(input("Kérem adja meg kör sugarát:"))
	n=float(input("Kérem adja meg a kör n számát:"))
	return float ((r*r)*n)


def teglalapKerulet():
	a=float(input("Kérem a téglalap egyik oldalát(kerület):"))
	b=float(input("Kérem a téglalap másik oldalát(kerület):"))
	return float(2*(a+b))

def teglalapTerulet():
	a=float(input("Kérem a téglalap egyik oldalát(terület):"))
	b=float(input("Kérem a téglalap másik oldalát(terület):"))
	return float(a*b)


def nyolcszogKerulet():
	a=float(input("Kérem a 8szög oldalát:"))
	return float(8*a)
	
def nyolcszogTerulet():
	a=float(input("Kérem a 8szög oldalát:"))
	b=float(input("Kérem adja meg a 8szög sugarát:"))
	return float (4*a*b)

szoveg=input("Milyen alakzattal szeretnél dolgozni? \n"
"1 - Háromszög \n"
"2 - Kör \n"
"3 - Téglalap \n"
"4 - Nyolcszög \n" )

if szoveg=="1":	
	haromszogKerulet()
	haromszogTerulet()
	derekszoguharomszogTerulet()

if szoveg=="2":
	korKerulet()
	korTerulet()

if szoveg=="3":
	teglalapKerulet()
	teglalapTerulet()

if szoveg=="4":
	nyolcszogKerulet()
	nyolcszogTerulet()










