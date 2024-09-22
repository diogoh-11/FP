def LoadFile(fname, veiculos, clientes):
    with open(fname, "r", encoding="utf-8") as file:
        for line in file:
            inf = line.strip().split(";")
            matri, marca, nif = inf

            veiculos[matri] = (marca, nif)

            if nif not in clientes:
                clientes[nif] = [matri]
            else:
                clientes[nif].append(matri)

        print(f"Foram importados {len(veiculos)} registros.")

    return 



def parque(veiculos):

    parque = sorted(veiculos.keys(), key = lambda t: (veiculos[t][1],t))
    for matri in parque:
        marca, nif = veiculos[matri]
        print(f"{nif}: ({matri}, {marca})")



def imprimirNif(clientes):

    for nif, matri in clientes.items():
        print(f"{nif} : {matri}")


def validar():
    
    while True:
        matricula = input("Matricula? ").upper()
        if len(matricula) == 8 \
            and matricula[0:2].isdigit() \
            and matricula[2] == '-' \
            and matricula[3:5].isalpha() \
            and matricula[5] == '-' \
            and matricula[6:8].isdigit():
            break

        else:
            print("Inválida")
    
    return matricula


def acessos(estacionamentos):

    matricula = validar()
    while True:
        tempo = input("Duração? ")
        if int(tempo) > 0 and tempo.isdigit():
            break
        else:
            print("Inválida\n")

    if matricula not in estacionamentos:
        estacionamentos[matricula] = []
    estacionamentos[matricula].append(tempo)


def escrever(estacionamentos):
    acessos =[]
    for matri in estacionamentos:
        for tempo in estacionamentos[matri]:
            acessos.append((tempo,matri))
    ace_ord = sorted(acessos, key = lambda t : t[0], reverse= True)

    with open("parque.csv", "w", encoding="utf-8")as file1:
        for tuplo in ace_ord:
            file1.write(f" {tuplo[0]};{tuplo[1]}\n")


def fatura(veiculos, clientes, estacionamentos):
    while True:
        nif = input("NIF? ")
        if nif not in clientes:
            break
        else:
            print("Nif inexistente!", end=" ")
    print(f"Fatura NIF : {nif}")
    print(f" {'Matricula':<15s} {'Marca':<10s}  {'Duração':>10s} {'Custo':>10s} ")
    total = 0
    for matri in clientes[nif]:
        if matri in estacionamentos:
            for tempo in estacionamentos[matri]:
                custo = int(tempo) * 0.01
                total += custo
                print("{:11s} {:11s} {:>11s} {:>8.2f}".format(matri, veiculos[matri][0], tempo, custo))
    print("{:11s} {:11s} {:>11s} {:>8.2f}".format("Total:", "", "", total))


    
         


def menu(veiculos,clientes, estacionamentos):
    while True:
        print("\n0 - Terminar")
        print("1 - Ler ficheiro clientes")
        print("2 - Imprimir clientes ordenados")
        print("3 - Mostrar matriculas por cliente")
        print("4 - Adicionar acessos ao parque")
        print("5 - Gravar acessos ao parque")
        print("6 - Gerar fatura para um cliente")
        op = int(input("Opção? "))

        while op not in range (0, 7):
            op = input("Opção invalida. Opção? ")
        
        if op == 0:
            break 

        elif op == 1:
            ficheiro = input("Nome do ficheiro? ")
            LoadFile(ficheiro, veiculos, clientes)

        elif op == 2:
            parque(veiculos)

        elif op == 3:
            imprimirNif(clientes)

        elif op == 4:
            acessos(estacionamentos)

        elif op == 5:
            if len(estacionamentos) != 0:
                escrever(estacionamentos)
                print("Ficheiro gravado com sucesso! ")
                print()

            else:
                print("Não existem entradas no parque! ")
                print()

        elif op == 6: 
            fatura(veiculos,clientes, estacionamentos)

def main():
    veiculos = {}
    clientes = {}
    estacionamentos = {}
    menu(veiculos, clientes, estacionamentos)

main()