distancia = float(input("Qual a distancia entre as duas cidades ? "))
v1 = float(input("v1? "))
v2 = float(input("v2? "))
t1 = distancia / v1
t2 = distancia / v2
v3 = str((2 * distancia )/ (t1 + t2))

print(" A velocidade média do percurso é de : "+(v3)+" m/s.")
