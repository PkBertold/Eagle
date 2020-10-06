#Elkezdhetünk ebbe dolgozni

def teglalapKerulet():
	a=float(input("Kérem a téglalap egyik oldalát(kerület):"))
	b=float(input("Kérem a téglalap másik oldalát(kerület):"))
	return float(2*(a+b))
<<<<<<< HEAD

=======
def teglalapTerulet():
	a=float(input("Kérem a téglalap egyik oldalát(terület):"))
	b=float(input("Kérem a téglalap másik oldalát(terület):"))
	return float(a*b)
print (teglalapKerulet())
print (teglalapTerulet())
>>>>>>> 03be70d538169ab87eb4673b1c4637f542afc92b
def triangle(a,b,c):
    print("perimeter: ",a+b+c)
triangle(3,4,5)

def triangle(a,b,c):
    print("ker: ",a+b+c)
a = input("a oldal: ")
b = input("b oldal: ")
c = input("c oldal: ")
triangle(a,b,c)

def nyolcszogKerulet():
	a=float(input("Kérem a 8szög oldalát:"))
	return float(8*a)
def nyolcszogTerulet():
	a=float(input("Kérem a 8szög oldalát")
	r=float(input("Kérem adja meg a 8szög sugarát:"))
	return float (4*a*r)
	
print("1 - Háromszög")
print("2 - Kör")
print("3 - Téglalap")
print("4 - Nyolcszög")
v=input("Milyen alakztattal szeretnél dolgozni?")
if v=="3":
	teglalapKerulet())
	teglalapTerulet())