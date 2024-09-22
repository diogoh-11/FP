def maiusculas(string):
    abr = []
    for mai in string:
        if mai.isupper():
            abr.append(mai)
    return ''.join(abr)
    
def main():
    entrada = input("Palavra: ")
    resultado = maiusculas(entrada)
    
    print("Big:", repr(entrada))
    print("Shorten:", repr(resultado)) 
    
if __name__ == "__main__":
    main()
    
            
    
