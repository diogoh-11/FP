import sys

#1
def LoadFile(fname):
    lst = []

    try:
        with open(fname,"r", encoding="utf-8") as file:
            head = file.readline()
            if not head.startswith('ranking,'):
                raise Exception('Wrong file format')
            for line in file:
                parts = line.strip().split(",")
                tup = (int(parts[0]), parts[1], parts[2], int(parts[3]), int(parts[4]),int(parts[5]), parts[6])

                lst.append(tup)
        return lst
    
    except FileNotFoundError:
        print("Ficheiro não encontrado!")



#2
def equipasPAIS(lst, pais, f = None):
    if f is None:
        f = sys.stdout

    for tup in lst:
        if tup[2] == pais:
            print('{:<30} {:>10} {:>20} {:10}'.format(tup[1],tup[2],tup[0],tup[3]),file=f)
    return


#3
def savePAIS(lst, pais, fname):
    with open(fname, "w", encoding="utf-8") as f:
        equipasPAIS(lst, pais, f)
        


#4
def paises(lst, pais):
    paises = {}
    for tup in lst:
        if tup [2] not in paises.keys():
            paises[tup[2]] = [tup[1]]
        else:
            paises[tup[2]].append(tup[1])
    print(paises[pais])


#5
def rank(lst):
    cresc = []
    for eq in lst:
        if eq[-1] == "+":
            cresc.append(eq)
    ordenada = sorted(cresc, key= lambda t: t[4], reverse = True)
    print(ordenada[0])
    

#6
def club(lst, clube):
    for eq in lst:
        if eq[1].lower() == clube.lower():
            print(f'\n{eq}')
            break
    else:
        print("\nClube não encontrado")


#7
def medrank(lst):
    ranking = {}
    for tup in lst:
        if tup [2] not in ranking.keys():
            ranking[tup[2]] = [int(tup[3])]
        else:
            ranking[tup[2]].append(int(tup[3]))

    for pais, ranks in ranking.items():
        media_rank = sum(ranks) / len(ranks)
        ranking[pais] = media_rank

    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1] ,reverse=True)

    # Imprimir os resultados ordenados
    print()
    print("Equipas ordenas por rank e suas devidas pontuações.\n")
    for pais, media_rank in ranking_ordenado:
        print(f'{pais}: {media_rank}')




#9
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

        op = input("Escolha uma opção de (0-6)")
        pos = ["1","2","3","4","5","6"]

        while op not in pos:
            print("Opção inválida!")
            op = input("Escolha uma opção de (0-6)")

        if op == "0":
            print("Programa encerrado. Até logo!")
            break

        elif op == "1":
            pais = input("Escolha um pais?")
            equipasPAIS(lst, pais)

        elif op == "2":
            pais = input("Escolha um pais?")
            savePAIS(lst, pais, f"{pais}.txt")

        elif op == "3":
            pais = input("Escolha um pais?")
            paises(lst, pais)

        elif op =="4":
            rank(lst)

        elif op == "5":
            clube = input("Insira um clube? ")
            club(lst,clube)

        elif op == "6":
            medrank(lst)

        else:
            print("Opção inválida. Tente novamente.")







def main():
    fname = "Soccer_Football Clubs Ranking.csv"
    lst = LoadFile(fname)
    menu(lst)

main()
