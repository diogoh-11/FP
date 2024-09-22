#a
def LoadFile(fname, veiculos, clientes):
    with open (fname, 'r' , encoding="utf-8") as f:
        for line in f:
            (matri,marca,nif) = line.rstrip().split(';')

            veiculos[matri] = (marca,nif)

            if nif not in clientes:
                clientes[nif] = []
            clientes[nif].append(nif)
        print('Foram importados {} registos'.format(len(veiculos)))
    return


#b
def imprimirParque(veiculos):

    parque = sorted(veiculos.keys(), key = lambda t: (veiculos[t][1],t))
    for matri in parque:
        (marca,nif) = veiculos[matri]
        print(nif, ":" ,(matri, marca))


#c
def imprimirNif(clientes):
    for nif in clientes:
        print(nif, ":" , clientes[nif])


#d
def validar():

    while True:
        matricula = input("Matricula ? ").upper()
        if len(matricula) == 8 \
                and matricula[0:2].isdigit() \
                and matricula[2] == '-' \
                and matricula[3:5].isalpha() \
                and matricula[5] == '-' \
                and matricula[6:8].isdigit():
                break
        else:
            print("Inválida!")  

    return matricula


#e
def acesso(estacionamento):
    mat = validar()
    tempo = input("Duração? ")

    while True:
        if tempo.isdigit() and int(tempo) > 0:
            break
        else:
            input("Invalido! Duração? ")
    
    if mat not in estacionamento:
        estacionamento[mat] = []
    estacionamento[mat].append(tempo)


#f
def escrever(estacionamentos):
    acessos =[]
    for matri in estacionamentos:
        for tempo in estacionamentos[matri]:
            acessos.append((tempo,matri))

    with open('parque.csv', 'w') as file1:
        for regis in sorted(acessos, key=lambda t: int(t[0]), reverse= True):
            file1.write("{};{}\n".format(regis[0],regis[1]))

    

#g
def fatura(veiculos,clientes,estacionamentos):
    while True:
        nif = input("NIF? ")
        if nif in clientes:
            break
        else:
            print('NIF inexistente!', end = ' ')
    print('Fatura NIF: {}'.format(nif))
    print('{:11s} {:11s} {:>11s} {:>8s}'.format('Matricula','Marca','Duracao','Custo'))
    total = 0
    for matri in clientes[nif]:
        if matri in estacionamentos:
            for tempo in estacionamentos[matri]:
                custo = int(tempo) * 0.01
                total += custo
                print("{:11s} {:11s} {:>11s} {:>8.2f}".format(matri, veiculos[matri][0], tempo, custo))
    print("{:11s} {:11s} {:>11s} {:>8.2f}".format("Total:", "", "", total))


#h
def menu():
    print("Opções disponíveis:")
    print('0 - Terminar')
    print('1 - Ler ficheiro de clientes')
    print('2 - Imprimir clientes ordenados')
    print('3 - Mostrar matriculas por cliente')
    print('4 - Adicionar acesso ao parque')
    print('5 - Gravar acessos ao parque')
    print('6 - Gerar fatura para um cliente')
    while True:
        op = input('Opcao? ')
        if op not in ['0','1','2','3','4','5','6']:
            print("Opcao invalida!", end=" ")
        else:
            break
    return op


def main():
    veiculos = {}
    clientes = {}
    estacionamentos = {}


    while True:
        op = menu()

        if op == "0":
            break

        elif op == "1":
            s = input("Digite o nome do seu ficheiro ")
            LoadFile(s,veiculos,clientes)
            print()

        elif op == "2":
            imprimirParque(veiculos)
            print()

        elif op == '3': 
            if len(clientes) > 0:
                imprimirNif(clientes)
            else:
                print('Não existem clientes!')

        elif op == "4":
            acesso(estacionamentos)
            print()

        elif op == "5":
            if len(estacionamentos) != 0:
                escrever(estacionamentos)
                print("Ficheiro gravado com sucesso! ")
                print()

            else:
                print("Não existem entradas no parque! ")
                print()

        elif op == '6':
            if len(clientes) != 0 and len(estacionamentos) != 0 and len(veiculos) != 0:
                fatura(veiculos,clientes,estacionamentos)
            else:
                print('Dados insuficientes para criar fatura!')


if __name__ == '__main__':
    main()


       
        


        