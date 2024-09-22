def intersect(a1, a2, b1, b2):
   assert a1 < b1
   assert a2 < b2
   
   if a1 >= b2 or a2 >= b1:
    print("False")
    return False
   else: 
    print("True")
    return True
def variaveis():
    a1 = float(input("Qual é o valor de a1: "))
    a2 = float(input("Qual é o valor de b1: "))
    b1 = float(input("Qual é o valor de a2: "))
    b2 = float(input("Qual é o valor de b2: "))
    return(a1, a2, b1, b2)   
    
a,b,c,d=variaveis()
intersect(a,b,c,d)
  
   
  
    
