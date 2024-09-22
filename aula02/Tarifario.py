tp = float(input("Quanto tempo durou a chamada em segundos : "))
pe = 0.12 + ((tp-60)*0.002) 
if tp < 60:
   print("Custo da chamada é de 0.12€")
else :
   print("Custo da chamada é de ",pe,"€")  
   
