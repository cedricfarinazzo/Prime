from config import *
import os
import math
import time

os.chdir(path)

if os.path.exist(name):
	with open(name, 'r') as fichier:
		 listechaine = fichier.read ()
	liste1 = listechaine.split ('\n')
	liste = []
	for element in liste1:
		liste.append(int(element))
	n = liste [-1] + 1
else:
	liste = [2,3]
	liste1 = ["2","3"]
	n = 4
i = 0
j = 0
compteur = 0


while True :
    j = 0
    d = 0
    diviseur = liste [d]
    racine_n = math.sqrt(n)
	len_liste = len (liste)-1
    while (diviseur < racine_n) and (d != len_liste):
        if (n%diviseur) !=0:
            j = 1
        elif (n%diviseur) == 0:
            j = 0
            break
        d += 1
        diviseur = liste [d]
    
    if j == 1 :
        liste.append (n)
        liste1.append (str (n))
        print (n)
        compteur += 1
    n += 1
    
    if compteur == 10000:
        liste2 = "\n".join(liste1)
        with open(name, 'w') as fichier:
             fichier.write (liste2)
        compteur = 0