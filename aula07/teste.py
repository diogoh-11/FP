data = {}
key = int(input("Enter key (0 to quit): "))
while key > 0 :  
   value = input("Enter value: ")
   data[key] = value
   size = len(data) 
   key = int(input("Enter key (0 to quit): "))
print(data)
print(data[3])