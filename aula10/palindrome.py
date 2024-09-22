def normalize(string):
    return "".join([char.casefold() for char in string if char.isalpha()])



def palindrome(string):
    string = normalize(string)

    if len(string) == 0 or len(string)  == 1:
        return True
    return string[0] == string[-1] and palindrome(string[1:-1])


def main():
    palindrome("Luz Azul")

main()