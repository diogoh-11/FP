import math

a = float(input("Qual é o comprimento de a? "))
b = float(input("Qual é o comprimento de b? "))

h = math.sqrt(a**2 + b**2)

angle = math.degrees(math.atan2(b, a))

print("Hipotenusa: {} ".format(h))
print("Valor do angulo entre a e b : {} ".format(angle))
