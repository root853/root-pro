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
  print("pas d'équation")
elif(a == 0 and (b != 0 and c!= 0)):
  print("il s'agit d'une équation du 1er degrée et nn d'une éqution du 2nd , on va donc calculer la seule solution de : bx + c = 0 ")
  print( (-c)/b )
else:
 if(D < 0):
   print("pas de solution réelle")
 elif(D == 0):
   print("on a une solution double x0")
   print( (-b)/(2*a) )
  
 else:
   print("vous avez bien deux soulutions réelles et distinctes")
   print( "les solutions sont : X1 =", ((-b) - sqrt(D))/(2*a), "\n X2=", ((-b) + sqrt(D))/(2*a) )
os.system("pause")