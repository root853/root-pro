n=int()
a=0
l=int()
liste=list()
sujet=list()
lon = input("le nombre de sujet\n")
while i< lon:
    sujet[i][0]=("input votre nom\n")
    sujet[i][1]=("input votre prenom\n")
    sujet[i][2]=("input votre age\n")
    sujet[i][3]=("input votre sexe\n")
    sujet[i][4]=("input votre profession\n")
    sujet[i][5]=("input votre taille\n")
    sujet[i][6]=("input votre poids\n")
    sujet[i][7]=("input votre pay\n")
    i=i+1
l=input(" mettez l=0 pour continuer\n")
while(l==0):
    n=input("donnez le numero du sujet")
    n=int(n)
    while a<8:
        print("voici les données", sujet[i][a])
        a = a+1

    
