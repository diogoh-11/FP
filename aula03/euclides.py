def variaveis():
    a = float(input("Qual o valor de a:"))
    b = float(input("Qual o valor de b:"))
    return (a,b)
def mdc(a,b):
    while (a != 0 or b != 0 or r != 0):
      r = a % b
      if r > 0: 
        a = b % r
        if r > 0:
         b = r % a
          
    print("b =",b)
a,b = variaveis()
mdc(a,b)

    
