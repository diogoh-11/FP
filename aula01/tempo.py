s = int(input("Quantos segundos? "))
m = int(s / 60)
h = int(s / 3600)
m1 = int((s - (h * 3600))/60)
s1 = int(s - (h * 3600) - (m1 * 60)) 

print("{}:{}:{}".format(h, m1, s1))