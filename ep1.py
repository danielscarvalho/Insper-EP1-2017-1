# -*- coding: utf-8 -*-

# Insper - Engenharia
# Design de Software - 2017.1
# EP1 - Solućãoo
import re

#Ajusta as conexões em letra minúscula
def fixConections(name):
    sufix=[" Do "," De "," Da "," Dos ", " E ", " Das "]
    for suf in sufix:
        name = name.replace(suf, suf.lower())
    return name

#ajusta nomes: remove espa�o no início e fim do nome
# coloca todos as palavras iniciando com letra maiúscula
def fixNames(name):
    return fixConections(re.sub("\s\s+" , " ", name).strip().title())

#remove nomes duplicados
def removeDuplicates(namesList):
    out = []
    for name in namesList:
        if name not in out:
            out.append(name)
    return out

#main: abre o arquivo e realiza loop principal
with open("nomes.txt", "r") as arquivo:
    lista_de_nomes = []
    for linha in arquivo:
        lista_de_nomes.append(fixNames(linha))

#remove nomes duplicados e exibe a lista na tela
for name in removeDuplicates(lista_de_nomes):
    print(name)