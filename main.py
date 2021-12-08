# Author: Mikołaj Mroczkowski
# GitHub Url: https://github.com/MikolajMroczkowski/sieveOfEratosthenes/tree/master
# Licese: GNU General Public License v3.0 (avalible in github repo)

def Sito(n):
    tab = list()
    for x in range(0,n):
        tab.append("T")
    tab[0]="F"
    tab[1]="F"
    for obj in range(2,int(n**0.5)+1):
        if tab[obj] == "T":
            for x in range(obj*obj,n,obj):
                tab[x] = "F"
    wyniki =""
    for x in range (len(tab)):
        if tab[x]=="T":
            wyniki += str(x)+" "
    return wyniki
print(Sito(1000))

