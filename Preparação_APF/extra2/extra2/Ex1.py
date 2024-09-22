import re

def validar_numero_telefone(numero):
    padrao = re.compile(r'^\+?[0-9]{3,}$')
    return bool(re.match(padrao, numero))


def registrar_chamada(chamadas):
    origem = input("Telefone origem? ")
    destino = input("Telefone destino? ")
    
    while not validar_numero_telefone(destino):
        print("Número de telefone destino inválido. Tente novamente.")
        destino = input("Telefone destino? ")

    duracao = (int(input("Duração (m)? ")) / 60)

    chamadas.append({"origem": origem, "destino": destino, "duracao": duracao})
    print("Chamada registrada com sucesso!")


def ler_ficheiro(chamadas):
    nome_ficheiro = input("Ficheiro? ")
    try:
        with open(nome_ficheiro, 'r') as file:
            for linha in file:
                dados = linha.split()
                origem, destino, duracao = dados[0], dados[1], int(dados[2])
                chamadas.append({"origem": origem, "destino": destino, "duracao": duracao})
        print("Chamadas lidas com sucesso.")
    except FileNotFoundError:
        print("Ficheiro não encontrado.")


def listar_clientes(chamadas):
    clientes = set()
    for chamada in chamadas:
        clientes.add(chamada["origem"])
        clientes.add(chamada["destino"])

    clientes_ordenados = sorted(clientes)
    print("Clientes:", " ".join(clientes_ordenados))


def calcular_custo_chamada(chamada):
    if chamada["destino"].startswith("2"):
        return chamada["duracao"] * 0.02
    elif chamada["destino"].startswith("+"):
        return chamada["duracao"] * 0.80
    elif chamada["origem"][:2] == chamada["destino"][:2]:
        return chamada["duracao"] * 0.04
    else:
        return chamada["duracao"] * 0.10


def gerar_fatura_detalhada(chamadas):
    numero_cliente = input("Número do cliente? ")
    chamadas_cliente = [chamada for chamada in chamadas if chamada["origem"] == numero_cliente]

    if not chamadas_cliente:
        print("Cliente não encontrado ou não realizou chamadas.")
        return

    total_custo = 0
    print("Fatura detalhada para o cliente", numero_cliente)
    for chamada in chamadas_cliente:
        custo_chamada = calcular_custo_chamada(chamada)
        total_custo += custo_chamada
        print(f"Destino: {chamada['destino']}, Duração: {chamada['duracao']}s, Custo: {custo_chamada:.2f} €")

    print(f"Custo total: {total_custo:.2f} €")


def main():
    chamadas = []

    while True:
        print("\nMenu:")
        print("1) Registar chamada")
        print("2) Ler ficheiro")
        print("3) Listar clientes")
        print("4) Fatura")
        print("5) Terminar")

        opcao = input("Opção? ")

        if opcao == "1":
            registrar_chamada(chamadas)
        elif opcao == "2":
            ler_ficheiro(chamadas)
        elif opcao == "3":
            listar_clientes(chamadas)
        elif opcao == "4":
            gerar_fatura_detalhada(chamadas)
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

