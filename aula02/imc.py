# -*- coding: utf-8 -*-

# Modifique o programa para indicar a categoria de IMC de acordo com a tabela:
# IMC:          <18.5   [18.5, 25[  [25, 30[    30 ou mais 
# Categoria:    Magro   Saudável    Forte       Obeso 

print("Índice de Massa Corporal")

altura = float(input("Altura (m)? "))
peso = float(input("Peso (kg)? "))

imc = int(peso / altura**2)

print("IMC:", imc, "kg/m2")

# Determinar a categoria de IMC:
if   imc <18.5:
    categoria = "Magro"
elif   18.5 <= imc < 25:
    categoria = "Saudavél"
elif 25 <= imc <30:
    categoria = "Forte"
elif 30 <= imc:
    categoria = "Obeso" 
#elif 40 <= imc:
   # categoria = b
    
#if categoria == b:
     #print("Uma baleia entrou na sala", categoria)
     #exit()

    
print("Categoria:", categoria)

