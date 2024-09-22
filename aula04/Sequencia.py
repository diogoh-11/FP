def inputTotal():
    s = 0.0
    t = 0
    while True:
        n = input("valor? ")
        if n == "": break   # if empty line, stop repeating!
        v = float(n)
        s += v
        t +=1
        med = s/t
    
    return med

# MAIN PROGRAM
def main():
    med = inputTotal()
    print(med)

if __name__ == "__main__":
    main()
