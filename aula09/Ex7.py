import math

import sys

def integrate(f, a, b, n):
    """The integral of f(x) for x between a and b.
    Approximated using the trapezoidal rule with n uniform subintervals."""
    assert n >= 1
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x_i = a + i * h
        result += f(x_i)
    result *= h
    return result

def example(n):
    # Function to integrate: (x - 2) / (x + 3)
    def f(x):
        return (x - 2) / (x + 3)

    a = 0.0  # Lower limit
    b = 1.0  # Upper limit

    # Calculate the integral using the integrate function
    result = integrate(f, a, b, n)
    return result

# Do not change the code below!
def evalPrint(expression):
    "Evaluate and print an expression and its result."
    result = eval(expression)
    print("{}\n--> {!r}".format(expression, result))

if __name__ == "__main__":
    evalPrint(" ".join(sys.argv[1:]))
    