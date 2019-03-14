import os
import argparse

def read(name):
    with open(name , 'r') as fichier:
        data = fichier.read()
    liste = data.split('\n')
    a = 0
    #b = 1
    l = -1
    for elm in liste:
        if elm != '':
            e = int(elm)
            a += e
            #b *= e
            l += 1

    print('Lenght :', l)
    print('Sum :', a)
    #print('Prod : ', b)
    print('Last Prime number : ', liste[-2])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Prime file")
    args = parser.parse_args()
    read(args.file)

if __name__ == '__main__':
    main()
