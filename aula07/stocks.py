
# Constantes para indexar os tuplos:
# Constantes para indexar os tuplos:
NAME, DATE, OPEN, MAX, MIN, CLOSE, VOLUME = 0, 1, 2, 3, 4, 5, 6

def main():
    lst = loadStockFile("nasdaq.csv")
    # Mostrar apenas os primeiros e últimos tuplos:
    print("Primeiro:", lst[1])
    print("Último:", lst[-1])
    
    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    for tup in lst:
        empresa = tup[NAME]
        volume = tup[VOLUME]
        totVol[empresa] = totVol.get(empresa, 0) + volume
    return totVol

def maxValorization(lst):
    vMax = {}
    for tup in lst:
        data = tup[DATE]
        empresa = tup[NAME]
        aber = tup[OPEN]
        fech = tup[CLOSE]
        valorizacao = (fech/aber - 1) * 100
        if data not in vMax or valorizacao > vMax[data][1]:
            vMax[data] = (empresa, valorizacao)

    return vMax

def stocksByDateByName(lst):
    dic = {}
    
    for tup in lst:
        data = tup[DATE]
        empresa = tup[NAME]
        
        # Verifica se a data já está no dicionário
        if data not in dic:
            dic[data] = {}

        # Adiciona a informação da empresa à data correspondente
        dic[data][empresa] = tup[2:]

    return dic

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0

    for empresa, num_acoes in portfolio.items():
        if empresa in stocks[date]:
            print(f"DEBUG: stocks[{date}][{empresa}] = {stocks[date][empresa]}")
            
            # Verifica se a tupla tem tamanho suficiente
            if len(stocks[date][empresa]) > CLOSE:
                fechamento_empresa = stocks[date][empresa][CLOSE]
                valor_empresa = fechamento_empresa * num_acoes
                val += valor_empresa
            else:
                print(f"WARNING: A tupla não tem o índice necessário para fechamento (CLOSE).")

    return val

if __name__ == "__main__":
    main()
