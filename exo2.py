# -*-coding:latin-1 -*
import os
a = 0
b = 0
c = 0
D = 0

a = input("saisissez votre nombre: ")
a = float( a )

b = input("saisissez votre nombre:")
b = float( b )
c = input("saisissez votre nombre:")
c = float( c )
D = ((b**2) - (4*a*c))
if((a == 0 and b == 0) and c == 0):
      print("pas d'Ã©quation")
elif(a == 0 and (b != 0 and c!= 0)):
      print("il s'agit d'une Ã©quation du 1er degrÃ©e et nn d'une Ã©qution du 2nd , on va donc calculer la seule solution de : bx + c = 0 ")
      print( (-c)/b )
else:
 if(D < 0):
      print("pas de solution rÃ©elle")
 elif D == 0:
      print("on a une solution double x0")
      print( (-b)/(2*a) )
  
 else:
   print("vous avez bien deux soulutions rÃ©elles et distinctes")
   if b < 0:
    X1 = X1 = ((-b) + sqrt(D))/(2*a)
    X2 = X2 = c/a/X1
 
    print(" les solutions sont : \n X1 =", X1, "\n X2 = ", X2 ) 
   else:
    X1 = X1 = ((-b) - sqrt(D))/(2*a)
    X2 = X2 = c/a/X1
    print( "les solutions sont : X1 =", ((-b) - sqrt(D))/(2*a), "\n X2=",  c/(a*(((-b) - sqrt(D))/(2*a))) ) 
os.system("pause")