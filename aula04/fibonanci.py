def fibonanci():
	a = int(input("Qual é o termo: "))
	t = 2
	n = 0
	s = 1
	if a == 1:
		s = 0
	elif a == 2:
		s ==1
	else:
	     while t < a:
		    nex = n + s
		    n = s
		    s = nex
		    t += 1
		      
print(f'O termo de ordem {a} é {s}')
fibonanci()
		



