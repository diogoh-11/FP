import sys

#1
def LoadFile(fname):
    lst = []
    with open(fname, "r", encoding="utf-8") as f:
        head = f.readline()
        for linha in f:
            parts = linha.strip().split(",")
            tup = (int(parts[0]), parts[1], parts[2], int(parts[3]), int(parts[4]),int(parts[5]), parts[6])

            lst.append(tup)
    return lst




#2
def ClubPais(Pais, lst, f =None):
    if f is None:
        f = sys.stdout

    for tuplo in lst:
        if tuplo[2] == Pais:
            print(f" {tuplo[1]:<20s} {tuplo[3]:<5} {tuplo[0]:<5}",file=f)
    


#3
def expPais(Pais, lst, fname):
    with open(fname, "w", encoding="utf-8")as f:
        ClubPais(Pais, lst, f)


#4
def paises(lst):
    d = {}
    for tuplo in lst:
        if tuplo[2] not in d:
            d[tuplo[2]] = [tuplo[1]]
        else:
            d[tuplo[2]].append(tuplo[1])
    print(d) 


#5
def rank(lst):
    lst2 = []
    for tuplo in lst:
        if tuplo[-1] == "+":
            lst2.append(tuplo)
    lst_ordenada = sorted(lst2, key = lambda t: t[4])
    print(lst_ordenada[-1])


#6
def search(lst,clube):
    for tuplo in lst:
        if tuplo[1] == clube:
            print(tuplo)
            break
    print("Não existe esse clube.")


#7
def rankmed(lst):
    d = {}
    for tuplo in lst:
        if tuplo[2] not in d:
            d[tuplo[2]] = [tuplo[0]]
        else:
            d[tuplo[2]].append(tuplo[0]) 

 
    for  pais, ranks in d.items():
        d[pais] = sum(ranks) / len(ranks)
        print(f" {pais} : {d[pais]}")

    d_ord = sorted(d.items(), key =lambda t: t[1], reverse=True)
    
    print()
    print("Equipas ordenas por rank e suas devidas pontuações.\n")
    for  lista in d_ord:
        print(f"{lista[0]} : {lista[1]}")
       
        
        





def menu(lst):
    while True:
        print("\n====Menu====")
        print("1. Mostrar clubes de um país")
        print("2. Salvar clubes de um país em um arquivo")
        print("3. Mostrar clubes por país")
        print("4. Mostrar melhor subida")
        print("5. Pesquisar clube")
        print("6. Mostrar média de ranking por país")
        print("0. Sair do programa")
        op = int(input("Opção? "))

        while op not in range (0,7):
            print("Opção Inválida!")
            op = int(input("Opção? "))
        
        if op == 0:
            break

        elif op == 1:
            pais = input("Escolha um país? ")
            ClubPais(pais, lst)

        elif op == 2:
            pais = input("Escolha um pais? ")
            expPais(pais,lst,f"{pais}.txt")

        elif op == 3:
            paises(lst)

        elif op == 4:
            rank(lst)

        elif op ==5:
            clube = input("Qual o clube? ")
            search(lst,clube)

        elif op ==6:
            rankmed(lst)




def main():
    ficheiro = "Soccer_Football Clubs Ranking.csv"
    lst = LoadFile(ficheiro)
    menu(lst)

main()
