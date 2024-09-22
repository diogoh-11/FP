
def primesUpTo(n):
    # Inicializa um conjunto com todos os números de 2 até n
    numbers = set(range(2, n + 1))
    
    # Itera pelos números de 2 até a raiz quadrada de n
    for i in range(2, int(n**0.5) + 1):
        # Se i está presente no conjunto, remove seus múltiplos
        if i in numbers:
            # Remove os múltiplos de i começando de i^2 até n
            numbers -= set(range(i**2, n + 1, i))
    
    return numbers

def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()

