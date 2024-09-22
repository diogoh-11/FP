def numeros():
    s = 0
    t = 0
    while True:
        n = input("Escolhe um número (pressione ENTER para terminar): ")
        if n == "":
            break
        elif not n.isdigit():  # Verificar se a entrada não é um dígito
            print("Insira um número válido.")
        else:
            s += float(n)
            t += 1

    if t > 0:
        m = s / t
        print(f"A média dos números é {m:.2f}")
    else:
        print("Nenhum número foi introduzido.")

numeros()
