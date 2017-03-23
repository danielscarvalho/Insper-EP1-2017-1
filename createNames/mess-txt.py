# Insper - Engenharia
# Design de Software - 2017.1
# EP1 - Geração de arquivo txt com nomes

import random

def messName(name):
    rNum = random.randint(1,7)

    if rNum == 1:
        return name.replace(" ", "  ")
    elif rNum == 2:
        return name + "    "
    elif rNum == 3:
        return name.lower()
    elif rNum == 4:
        return name.upper()
    elif rNum == 5:
        return name
    elif rNum == 6:
        return "    " + name
    elif rNum == 7:
        return name.replace(" ", "   ")

lista_de_nomes = []


with open("nomes-big.txt", "r", encoding="utf8") as arquivo:
    for linha in arquivo:
        lista_de_nomes.append(messName(linha))

random.shuffle(lista_de_nomes) #Embaralha a coisa toda!

#Salva
with open ("nomes-big-mass.txt","w", encoding="utf8") as fp:
    for name in lista_de_nomes:
        fp.write(name)
