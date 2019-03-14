import os
import math
import time
import argparse

def gen(name):
    liste = [2,3]
    n = 4
    llen = 2
    if os.path.exists(name):
        with open(name, 'r') as f:
            data = f.read()
        liste1 = data.split('\n')
        liste = []
        for e in liste1:
            if e != '':
                liste.append(int(e))
        n = liste [-1] + 1
        llen = len(liste) - 1
    data = ''
    
    while True :
        isPrime = True
        di = 0
        
        while (liste[di] * liste[di] <= n) and (di < llen) and isPrime:
            isPrime = (n%liste[di]) != 0
            di += 1
        if isPrime:
            liste.append(n)
            data += str(n) + "\n"
            llen += 1
            print(n)
        n += 1
    
        if llen % 100000 == 0:
            with open(name, 'a') as f:
                f.write(data)
                data = ''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Prime file")
    args = parser.parse_args()
    gen(args.file)

if __name__ == '__main__':
    main()
