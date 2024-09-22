import math

def floatInput(prompt, min=None, max=None):
    res = float(input(prompt))
    while True:
        try:
            res = float(input(prompt))
            if (min is None or res >= min) and (max is None or res <= max):
                return res
            else:
                print(f"ERROR: Value must be between {min} and {max}.")
        except ValueError:
            print("ERROR: Not a float!")

def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    h = floatInput("Humidity (%)? ", 0, 100)
    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", min=-273.15)
    print("t:", t)

    # d) Now, the corrected section:
    impossible = floatInput("Value in [0, 3]? ", min=0, max=3)
    
    return

if __name__ == "__main__":
    main()