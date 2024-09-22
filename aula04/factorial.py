def factorial(n):
   assert isinstance(n, int), "n should be an int"
   assert n >= 0            , "n should not be negative"
   f = 1
   while n >= 1:
      f *= n
      n -=1
   print(f) 
factorial(int(input("Qual é o número pretendido: ")))

