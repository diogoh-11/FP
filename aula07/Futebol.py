def equipas():   
    equipa = str(input("Qual é o nome da equipa: "))
    teams = []
    while equipa != "":
        teams.append(equipa)
        equipa = str(input("Qual é o nome da equipa: "))
    
    return teams


def allMatches(teams):
    assert len(teams) >= 2, "Requires two or more teams!"

    matches = []

    for i in range(len(teams)):
        for j in range(len(teams)):
            if i != j:
                match = (teams[i], teams[j])
                matches.append(match)

    return matches


def resultados(matches):
    tabela = {equipa: [0, 0, 0, 0, 0, 0] for equipa in set(sum(matches, ()))}

    for jogo in matches:
        equipa_a, equipa_b = jogo
        resultado_a, resultado_b = map(int, input(f'Qual foi o resultado do jogo {jogo} (gols equipa A, gols equipa B): ').split())

        # Atualiza os registros para a equipa A
        tabela[equipa_a][3] += resultado_a  # Gols marcados
        tabela[equipa_a][4] += resultado_b  # Gols sofridos

        # Atualiza os registros para a equipa B
        tabela[equipa_b][3] += resultado_b  # Gols marcados
        tabela[equipa_b][4] += resultado_a  # Gols sofridos

        # Atualiza o número de vitórias, empates e derrotas
        if resultado_a > resultado_b:
            tabela[equipa_a][0] += 1  # Vitória para equipa A
            tabela[equipa_b][2] += 1  # Derrota para equipa B
            tabela[equipa_a][5] += 3  # Pontos para equipa A
        elif resultado_a < resultado_b:
            tabela[equipa_b][0] += 1  # Vitória para equipa B
            tabela[equipa_a][2] += 1  # Derrota para equipa A
            tabela[equipa_b][5] += 3  # Pontos para equipa B
        else:
            tabela[equipa_a][1] += 1  # Empate para equipa A
            tabela[equipa_b][1] += 1  # Empate para equipa B
            tabela[equipa_a][5] += 1  # Pontos para equipa A (empate)
            tabela[equipa_b][5] += 1  # Pontos para equipa B (empate)

    return tabela


def exibirTabela(tabela):
    print("{:<10} {:<8} {:<8} {:<8} {:<15} {:<15} {:<8}".format(
        "Equipa", "Vitórias", "Empates", "Derrotas", "Golos Marcados", "Golos Sofridos", "Pontos"
    ))
    
    # Ordena a tabela por pontos em ordem decrescente
    tabela_ordenada = sorted(tabela.items(), key=lambda x: x[1][5], reverse=True)

    for equipa, dados in tabela_ordenada:
        print("{:<10} {:<8} {:<8} {:<8} {:<15} {:<15} {:<8}".format(
            equipa, dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]
        ))

def equipa_campea(tabela):
    # Ordena a tabela por pontos em ordem decrescente
    tabela_ordenada = sorted(tabela.items(), key=lambda x: x[1][5], reverse=True)

    # Verifica se há empate e, em caso afirmativo, usa a diferença de golos como critério
    equipas_empatadas = [equipa for equipa, dados in tabela_ordenada if dados[5] == tabela_ordenada[0][1][5]]
    if len(equipas_empatadas) > 1:
        equipa_campea = max(equipas_empatadas, key=lambda x: tabela[x][3] - tabela[x][4])
    else:
        equipa_campea = tabela_ordenada[0][0]

    return equipa_campea



def main():
    jogos = allMatches(equipas())
    tabela = resultados(jogos)
    exibirTabela(tabela)


    # Determinar e exibir a equipa campeã
    campea = equipa_campea(tabela)
    print(f"A equipa campeã é: {campea}")


if __name__ == "__main__":
    main()

