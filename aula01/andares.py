A3 = 9
A2 = 6
A1 = 3
M = 2
vm = 3600               #velocidade em metros por hora
d1 = (M*(A1+A2+A3))*2   #distancia percorrida num dia
d356 = (356 * d1)/1000  # distancia percorrida num ano em kilometros
print("Distancia percorrida em Kilometros : {} ".format(d356))
t = (d356*1000)/vm      #tempo de funcionamento em horas
print("Tempo de funcionamento do elevador em horas: {}".format(t))
