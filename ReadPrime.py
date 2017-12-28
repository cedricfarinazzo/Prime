from config import *
import os
import math
import time

os.chdir(path)

try:
	with open(name , 'r') as fichier:
		 listechaine = fichier.read ()
	liste1 = listechaine.split ('\n')
	time.sleep(2)
	liste = []
	for element in liste1:
		liste.append(int(element))
	a = 0
	b = 1
	for element in liste:
		a += element
		b *= element
		print (b,'\n')
	b += 1
	print('\n\nLenght : ',len (liste),'\nSum : ',a,'\nProd : ',b,'\nLast Prime number : ',liste [-1])
	time.sleep(3)
	break
except:
	pass