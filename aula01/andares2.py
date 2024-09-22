A = int(input("Quantos andares tem o prédio:"))
d1 = (3+(3*A))*A*2                     
vm = 3600                    # velocidade em metros por hora  
d365 = (365 * d1)/1000
print("Distancia percorrida em Kilometros: {} ".format(d365))
t = (d365*1000)/vm           #tempo de funcionamento em horas
print("Tempo de funcionamento do elvador em horas: {}".format(t))
