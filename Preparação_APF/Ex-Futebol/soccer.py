import sys

#1
def loadFile(fname):
    lst = []

    with open(fname, encoding='utf-8') as f:
        head = f.readline()
        if not head.startswith('ranking,'):
            raise Exception('Wrong file format')
        for line in f:
            #print(repr(line)) #imprime a representação da linha
            #print(line)
            line = line.strip()
            parts = line.split(',')
            #print(parts)
            tup = (int(parts[0]), parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]), parts[6])
            lst.append(tup)

    return lst

#2
def country_clubs(country, lst, f = None):     #f = sys.stdout serev para imprimir a função num determinado ficheiro dado como argumento neste caso imprime no terminal pois não se esta a dar nenhum argumento mas quando se utliza a função a seguir já se esta a dar um argumento logo vai imprimir num ficheiro dado. 
    if f is None:
        f = sys.stdout   # colocado para resolver problemasem relação ao menu

        
    for eq in lst:
        if eq[2] == country:
            print('{:^30s} {:^30s} {:8d} {:8d}'.format(eq[1], eq[2], eq[0], eq[3]), file=f)

    return

#3
def saveCountry(lst, country, fname):
    with open(fname, 'w', encoding='utf-8') as f:
        country_clubs(country, lst, f)

#4
def clubsByCountry(lst):
    dic = {}
    for eq in lst:
        club = eq[1]
        pais = eq[0]
        if pais in dic:
            dic[pais].append(club)
        else:
            dic[pais] = [club]
    return dic

#5
def bestRise(lst):
    cresc = []
    for eq in lst:
        if eq[-1] == "+":
            cresc.append(eq)
    cresc_ordenada = sorted(cresc, key= lambda t: t[4])
    print(cresc_ordenada[-1])


#6
    
def Club(lst,club):
    equipa = []
    for eq in lst:
        if eq[1].lower() == club.lower():
            equipa.append(eq)
            break
    else:
        nova = input("Equipa não encontrada. Por favor insira outra. ")
        return Club(lst,nova)
    print(equipa)
            

#7
'''criar um dicionario com um para a soma dos ranks e outro '''
def ranks(lst):
    ranking = {}
    for eq in lst:
        rank = eq[3]
        pais = eq[2]
        if pais in ranking:
            ranking[pais].append(rank)
        else:
            ranking[pais] = [rank]
    
    for pais, ranks in ranking.items():
        media_rank = sum(ranks) / len(ranks)
        ranking[pais] = media_rank

    # Ordenar os resultados por média de rank
    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1] ,reverse=True)

    # Imprimir os resultados ordenados
    print()
    print("Equipas ordenas por rank e suas devidas pontuações.\n")
    for pais, media_rank in ranking_ordenado:
        print(f'{pais}: {media_rank}')
    
#9
def menu(lst):
    while True:
        print("\n===== Menu =====")
        print("1. Mostrar clubes de um país")
        print("2. Salvar clubes de um país em um arquivo")
        print("3. Mostrar clubes por país")
        print("4. Mostrar melhor subida")
        print("5. Pesquisar clube")
        print("6. Mostrar média de ranking por país")
        print("0. Sair do programa")

        opcao = input("Escolha uma opção (0-6): ")

        if opcao == '0':
            print("Programa encerrado. Até logo!")
            break
        elif opcao == '1':
            country = input("Digite o país: ")
            country_clubs(country, lst)
        elif opcao == '2':
            country = input("Digite o país: ")
            saveCountry(lst, country, f'{country}.txt')
        elif opcao == '3':
            print(clubsByCountry(lst))
        elif opcao == '4':
            bestRise(lst)
        elif opcao == '5':
            club = input("Qual equipa queres pesquisar? ")
            Club(lst, club)
        elif opcao == '6':
            ranks(lst)
        else:
            print("Opção inválida. Tente novamente.")
    
    



def main():
    #fname = input('File? ')
    fname = 'Soccer_Football Clubs Ranking.csv'
    lst = loadFile(fname)
    menu(lst)


if __name__ == '__main__':
    main()