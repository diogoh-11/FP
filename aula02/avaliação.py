CTP = float(input("Qual foi a nota da CTP:"))
CP = float(input("Qual foi a nota da CP:"))
NF = 0.3*CTP + 0.7*CP
if (CTP or CP) < 6.5:
    print("NF=66")
else:
    print("NF:", NF)
if NF < 10:
    ATPR = float(input("Qual foi a nota da ATPR:"))    
    APR = float(input("Qual foi a nota da ATPR:"))
    NR = 0.3*max(CTP,ATPR) + 0.7*max(CP,APR)
    print("NR:", NR)
     
