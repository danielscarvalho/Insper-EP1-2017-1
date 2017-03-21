# Insper - Engenharia
# Design de Software - 2017.1
# EP1 - Solu��o

#Ajusta as conex�es em letra min�scula
def fixConections(name):
    sufix=[" De "," Da "," Dos "]
    for suf in sufix:
        name = name.replace(suf, suf.lower())
    return name

#ajusta nomes: remove espa�o no in�cio e fim do nome
# coloca todos as palavras iniciando com letra mai�scula
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
print(removeDuplicates(lista_de_nomes))