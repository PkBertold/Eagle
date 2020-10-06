#Elkezdhetünk ebbe dolgozni
def TeglalapKerulet():
    a=float(input("kérem adja meg a téglalap a oldalát(kerület)[cm]:"))
    b=float(input("kérem adja meg a téglalap b oldalát(kerület)[cm]:"))
    return float(2*(a+b))
def TeglalapTerulet():
    a=float(input("kérem adja meg a téglalap a oldalát(terület)[cm]:"))
    b=float(input("kérem adja meg a téglalap a oldalát(terület)[cm]:"))
    return float(a*b)
print (TeglalapTerulet())
print (TeglalapKerulet())  