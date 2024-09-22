
# Generates all length-3 words with symbols taken from the given alphabet.
def genWords3(symbols):
    return [ x+y+z for x in symbols for y in symbols for z in symbols ]


# Generates all length-n words with symbols taken from the given alphabet.

def genWords(symbols, n):
    if  n == 0:
        return ['']
    else:
        return [x+y for x in genWords(symbols, n-1) for y in symbols]


def main():
    lstA = genWords3("abc")
    print(lstA)

    lstB = genWords("abc", 3)  # should return the same words, maybe in other order
    print(lstB)
    assert sorted(lstA) == sorted(lstB)

    lstC = genWords("0123", 4)  # should return all length-4 binary words
    print(lstC)

if __name__ == "__main__":
    main()

