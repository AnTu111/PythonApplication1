#Ülesanne 1
name = str(input("Введите свое имя"))
print("Привет, " + name)

#Ülesanne 2
calculate = float(3+8/(4-2)*4)
print(calculate)

#Ülesanne 2.1
r=int(3)
d=r*r
ruudupindala = d*d
ruuduumbermõõt = 4*d
π=3.14 
ringipindala = round(π*d)
ringiumbermoot = round(2*π*r)
print(d + ruudupindala + ruuduumbermõõt + ringipindala +ringiumbermoot)
print(d)
print(ruudupindala)
print(ruuduumbermõõt)
print(ringipindala)
print(ringiumbermoot) 

#Ülesanne 2.2
maaraadius = float(6378000) # või 6378 km
müntiraadius = float(0.02575) # või 27,75 mm
π = 3.14 
ümbermõõt = 2*π*maaraadius
print("длина окружности")
print(ümbermõõt/1000,"km")
print(round((ümbermõõt/müntiraadius)/1000),"km")

#Ülesanne 3
text1=str("kill")
text2=str("koll")
text3=str("killadi")
print(text1 + "-" + text2+" "+text1 + "-" + text2+" "+text3+"-"+text2+" "+text1 + "-" + text2+" "+text1 + "-" + text2+" "+text3+"-"+text2+" "+
text1 + "-" + text2)

#Ülesanne 4
number=(print("Rong see sõitis tsuhh tsuhh tsuhh\npiilupart oli rongijuht.\nRattad tegid rat tat taa,\nrat tat taa ja tat tat taa.\nAga seal rongi peal,\nkas sa tead, kes olid seal?"))




#Ülesanne 5
a=float(input("Введите длину стороны а"))
b=float(input("Введите длину стороны b"))
pindala=float(2*(a+b))
ümbermõõdu=float(a*b)
print("Pindala on", pindala)
print("Ümbermõõt on ", ümbermõõdu)