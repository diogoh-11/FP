# Complete o programa!

# a)
def loadFile(fname, lst):
    ficheiro = open(fname, 'r')
    linha1 = True
    for line in ficheiro:
        if linha1:
            linha1 = False
            continue
        linha = line.split('\t')
        identificação = (int(linha[0]), linha[1],float(linha[5]),float(linha[6]),float(linha[7]))
        lst.append(identificação) 
    print(str(lst))
    ficheiro.close()
    return lst

      
# b) Crie a função notaFinal aqui...
def notaFinal(fname):
    return sum(reg[2:])/3

# c) Crie a função printPauta aqui...
def printPauta(lst):
    

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    ...
    
    # mostrar a pauta
    ...


# Call main function
if __name__ == "__main__":
    main()


