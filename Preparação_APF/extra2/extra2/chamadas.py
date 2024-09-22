def validar():
    while True:
        tel_or = input("Telefone de origem? ")
        if len(tel_or) in range(3,10) and (tel_or.isdigit() or tel_or[0] == "+" and tel_or[1:].isdigit()):
            break
        else:
            print("Inválido!")

    while True:
        tel_des = input("Telefone de destino? ")
        if len(tel_des) in range(3,10) and (tel_des.isdigit() or tel_des[0] == "+" and tel_des[1:].isdigit()):
            break
        else:
            print("Inválido!")

    return tel_or,tel_des


def registar():
    lst = []
    tel_or,tel_des = validar()
    while True:
        dur = int(input("Duração (s)? "))
        if  dur > 0:
            break
        else:
            print("Duração inválida")
    lst.append([tel_or,tel_des,dur])
    return lst


def LoadFile(fname):
    try:
        lst = []
        with open(fname,"r", encoding="utf-8") as f:
            for line in f:
                parts = line.split()
                tel_or,tel_des,dur = parts[0], parts[1], parts[2]
                lst.append([tel_or,tel_des,dur])
        return lst
    
    except FileNotFoundError:
        print("Ficheiro não encontrado!")




def listar(lst):
    clientes = []
    for lista in lst:
        if lista[0] not in clientes:
            clientes.append(lista[0])
    clientes_ordenados = sorted(clientes)
    print(f"Clientes {clientes_ordenados}")
    return clientes



def preço(tel):
    if tel.startswith("2"):
        preço = 0.02
    elif tel.startswith("+"):
        preço = 0.8
    elif tel[0] == tel[1]:
        preço = 0.04
    else:
        preço = 0.1
    return preço



def fatura(numero, reg):
    lst2 = []
    total_tempo = 0
    total_custo = 0

    for lista in reg:
        if numero in lista:
            duracao = int(lista[2])
            destino = lista[1]
            custo_por_minuto = preço(destino)
            custo_chamada = (duracao / 60) * custo_por_minuto
            total_tempo += duracao
            total_custo += custo_chamada

            print(f'{"Duração":<20s} {"Duração":<20s} {"Custo":<10s}')
            print(f"{destino:<20s} {duracao:<20d} {custo_chamada:<10.2f}")

    print(f"Total:               {total_tempo} minutos                 {total_custo:.2f} €")



def menu():
    reg = []
    lst = []

    while True: 
        print("\n1) Registrar chamada")
        print("2) Ler ficheiro")
        print("3) Listat clientes")
        print("4) Fatura")
        print("5) Terminar")
        op = int(input("Opção? "))
        while op not in range(0,6):
            print("Opção inválida!")
            op = int(input("Opção? "))


        if op == 5:
            break

        elif op == 1:
            reg += registar()

        elif op == 2:
            ficheiro = "chamadas1.txt"
            lst = LoadFile(ficheiro)

        elif op == 3:
            listar(lst)

        elif op == 4:
            numero = input("Cliente? ")
            fatura(numero, reg)



def main():
    menu()

main()