"""
def primo():
   for n in range(1,100): 
	   for num in (2,9):
		   r = n % num
		   if r == 0:
			   print("O número",n," é não primo.")
			   break
		   if num == 100 and r != 0 and n == 1:
			   print("O número",n,"é primo.")
			   break
            
primo()
"""


def primo():
    for n in range(2, 100):
        is_prime = True  # Assumimos que n é primo até que se prove o contrário
        for num in range(2, int(n**0.5) + 1):
            if n % num == 0:
                is_prime = False  # Encontramos um divisor, portanto, n não é primo
                break
        if is_prime:
            print("O número", n, "é primo.")

primo()
		      
