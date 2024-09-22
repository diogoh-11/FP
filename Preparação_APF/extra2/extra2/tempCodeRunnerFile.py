
    while not (0 < int(jornada) <= 13):
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
            resul.append((numero,aposta))

    with open(f'jornada{jornada}.csv', "w") as file1: