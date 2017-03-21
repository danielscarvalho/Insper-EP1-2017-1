# -*- coding: utf-8 -*-

# Versão simplificada da solução do EP1

#main: abre o arquivo e realiza loop principal
with open("nomes.txt", "r") as arquivo:
    lista_de_nomes = []
    for linha in arquivo:
        lista_de_nomes.append (linha)

# Lista de conectivos conhecidos
conectivos = ['Da', 'Das', 'De', 'Do', 'Dos']

# Percorre lista de nomes, titulando e ajustando conectivos
lista_titulada = []
for nome in lista_de_nomes:
    # Titula os nomes -- tudo em minúsculas, exceto a inicial
    nome = nome.title ()
    
    # Quebra o nome completo em palavras distintas
    nomes = nome.split ()
    for ind in range (len (nomes)):
        # Se uma das palavras do nome for um conectivo
        if nomes[ind] in conectivos:
            # Minuscula o nome
            nomes[ind] = nomes[ind].lower ()
    
    # Acrescenta o nome tratado à lista de nomes titulados
    lista_titulada.append (" ".join (nomes))

# Ordena lista de nomes
lista_titulada = sorted (lista_titulada)

# Imprime nomes, 
print (lista_titulada[0])
for ind in range (len (lista_titulada) - 1):
    if lista_titulada[ind] != lista_titulada[ind + 1]:
        print (lista_titulada[ind + 1])
