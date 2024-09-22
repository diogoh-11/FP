def LoadJornadas(fname):
    try:
        lst = []
        with open(fname,"r") as file:
            for line in file:
                (jor,casa,fora) = line.strip().split(",")
                lst.append((jor,casa,fora))
        return lst
    
    except FileNotFoundError:
        print("Ficheiro não encontrado")


def LoadJogos(ficheiro):
    try:
        jogos = []
        with open(ficheiro,"r") as file2:
            for line in file2:
                jogo_info = line.strip().split(",")
                jogos.append(jogo_info)
        return jogos
    except FileNotFoundError:
        print("Ficheiro de jogos não encontrado")


def Aposta(lst,jogos):
    while True:
        vezes = 0

        jornada = input("Jornada? ")

        if jornada == "0":
            break

        while not (0 <= int(jornada) <= 13):
            print("Invalido!")
            jornada = input("Jornada? ")

        
        resul = []
        numero = 0
        for tuplo in lst:
            if tuplo[0] == jornada:
                numero += 1
                aposta = input(f"{numero} {tuplo[1]} vs {tuplo[2]}: ")
                while aposta not in {'1', '2', 'X'}:
                    print("Aposta inválida! Use '1' para time da casa, '2' para time visitante ou 'X' para empate.")
                    aposta = input(f"{numero} {tuplo[1]} vs {tuplo[2]}: ")
                resul.append((tuplo[1],tuplo[2],numero,aposta))


        with open(f'jornada{jornada}.csv', "w") as file1:
            for resultado in resul:
                file1.write(f"{resultado[2]}, {resultado[3]}\n")

        print(f"\nJornada {jornada}")


        realidade = ""
        aposta = ""
        acertos = 0
        for resultado in resul:
            for jogo in jogos:
                if jogo[1] == resultado[0] and jogo[2] == resultado[1]:
                    if int(jogo[-2]) > int(jogo[-1]):
                        realidade = "1"
                    elif int(jogo[-1]) > int(jogo[-2]):
                        realidade = "2"
                    elif int(jogo[-1]) == int(jogo[-2]):
                        realidade = "X"
                    if realidade == resultado[3]:
                        aposta = "(Certo)"
                    else:
                        aposta = "(Errado)"
                    print(f"{resultado[2]:<3} {resultado[0]:<20} {jogo[3]}-{jogo[4]:<5} {resultado[1]:<20} : {resultado[3]} {aposta:>8}")

                    if aposta == "(Certo)":
                        acertos += 1

        print(f"Tem {acertos} certas")

        premio = 0

        if acertos < 7:
            print("Sem prémio")
            premio += 0

        elif  6 < acertos < 8:
            print("3º prémio")
            premio += 100

        elif  7 < acertos < 9:
            print("2º prémio")
            premio += 1000

        elif  acertos == int(resultado[2]):
            print("1º prémio")
            premio += 5000
        
        vezes += 1


    return premio, vezes



def calcular_premio(premio, vezes):

    saldo = 0
    for n in range(vezes):
        saldo -=0.4
    
    saldo_final = saldo + premio 

    print(f"Saldo! {saldo_final} euros")



def main():

    ficheiro = "Jornadas.csv"
    lst = LoadJornadas(ficheiro)
    jogos = LoadJogos("Jogos.csv")
    premio, vezes = Aposta(lst,jogos)
    calcular_premio(premio, vezes)


main()