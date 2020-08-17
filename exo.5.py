d = list()
i = int(0)
l=int(0)
p=int(0)
a = input("le nombre de mot \n")
a=int(a)
for i in range(a):
    d[i] = input(" donnez votre mot\n")
    i=i+1
for l in range(a):
    print(d[0])
    for p in range(1, l):
        if d[l] == d[p]:
            print(d[l])
            b=b+1
            l=l+1
print("le nombre de mots distinct est ", l+1)            
