
Pedro_c1=int(input("ingrese el capital de pedro: "))
Juan_c2=int(input("ingrese el capital de juan: "))
Inversion_c3= int(input("ingrese el capital necesario para la inversion "))

a= Pedro_c1+Juan_c2
n=0

while a<Inversion_c3:
 
Pedro_c1= Pedro_c1+(Pedro_c1*0.03)
Juan_c2=Juan_c2+(Juan_c2*0.04)
a= Pedro_c1+Juan_c2
n=n+1

print("Nececuita" +str(n)"+ meses") 
