# Complete este programa como pedido no guião da aula.
def addC(contactos):
    num = str(input("Qual é o número: "))
    while len(num) != 9:
        print("Número inválido! ")
        num = str(input("Qual é o número: "))
    pess = str(input("Qual é o nome da pessoa: "))
    contactos[num] = pess


def removeC(contactos):
    num = str(input("Qual é o número: "))
    while len(num) != 9:
        print("Número inválido! ")
        num = str(input("Qual é o número: "))
    contactos.pop(num)


def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^30s} : {:<30s}".format("Numero", "Nome", "Morada"))
    for num, info in dic.items():
        print("{:>12s} : {:^30s} : {:<30s}".format(num, info["Nome"], info["Morada"]))


def proC(contactos):
    num = input("Mete um número de telefone: ")
    while len(num) != 9 or not num.isdigit():
        print("Número inválido! Coloca um número com 9 carateres.")
        num = input("Mete um número de telefone: ")

    name = contactos.get(num)

    if name:
        print(f"O número: {num} é de {name}")
    else:
        print("Contacto não encontrado.")


def filterPartName(contactos):
    partName = input("Digite parte do nome: ")
    matching_contacts = {key: value for key, value in contactos.items() if partName.lower() in value.lower()}

    print("Contactos que contêm '{}' no nome:".format(partName))
    listContacts(matching_contacts)


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": {"Nome": "Universidade de Aveiro", "Morada": "Santiago, Aveiro"},
                 "727392822": {"Nome": "Cristiano Aveiro", "Morada": "Coimbra"},
                 "387719992": {"Nome": "Maria Matos", "Morada": "Viseu"},
                 "887555987": {"Nome": "Marta Maia", "Morada": "Coimbra"},
                 "876111333": {"Nome": "Carlos Martins", "Morada": "Porto"},
                 "433162999": {"Nome": "Ana Bacalhau", "Morada": "Salomão"}
                 }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            print("Adicionar contacto")
            addC(contactos)
        elif op == "R":
            print("Remover Contacto")
            removeC(contactos)
        elif op == "N":
            print("Procurar Contacto")
            proC(contactos)
        elif op == "P":
            print("Procurar parte do nome")
            filterPartName(contactos)
        else:
            print("Não implementado!")


# O programa começa aqui
main()
