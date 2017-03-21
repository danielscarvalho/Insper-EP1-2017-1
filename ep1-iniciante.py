# -*- coding: utf-8 -*-

# Versão simplificada da solução do EP1

#main: abre o arquivo e realiza loop principal
with open("nomes.txt", "r") as arquivo:
    lista_de_nomes = []
    for linha in arquivo:
        lista_de_nomes.append (linha)

conectivos = ['Da', 'Das', 'De', 'Do', 'Dos']

# Percorre lista de nomes, titulando e ajustando conectivos
lista_titulada = []
for nome in lista_de_nomes:
    nome = nome.title ()
    nomes = nome.split ()
    for ind in range (len (nomes)):
        if nomes[ind] in conectivos:
            nomes[ind] = nomes[ind].lower ()
    
    lista_titulada.append (" ".join (nomes))

# Ordena lista de nomes
lista_titulada = sorted (lista_titulada)

# Imprime nomes, 
print (lista_titulada[0])
for ind in range (len (lista_titulada) - 1):
    if lista_titulada[ind] != lista_titulada[ind + 1]:
        print (lista_titulada[ind + 1])
