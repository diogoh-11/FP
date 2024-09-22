def openfile():
    texto = open('names.txt', 'r')
    txt = texto.readlines()

    return txt

texto = openfile()
d = {}
n = True
for l in texto:
    if n == True:
        n = False
        continue
    linha = l.strip()
    abc = linha.split(" ")
    if abc[-1] in d.keys():
        d[abc[-1]].append(abc[0])
    else:
        d[abc[-1]] = [abc[0]]

for key in d.keys():
    values_str = ', '.join(d[key])
    print(f"{key} : {{{values_str}}}")

def main():
    texto = openfile()
    d = {}
    n = True
    for l in texto:
        if n == True:
           n = False
           continue
        linha = l.strip()
        abc = linha.split(" ")
        if abc[-1] in d.keys():
           d[abc[-1]].append(abc[0])
        else:
           d[abc[-1]] = [abc[0]]

    for key in d.keys():
        values_str = ', '.join(d[key])
        print(f"{key} : {{{values_str}}}")

main()
