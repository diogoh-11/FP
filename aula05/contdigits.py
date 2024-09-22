def countDigits(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count
    
def main():
    string = input()
    
    print("string:", string)
    print("result:", countDigits(string) )
    
if __name__ == "__main__":
    main()


    
