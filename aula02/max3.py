# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with a conditional statement (if / if-else) instead?

x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input("number? "))

maiornum = "x1"
if x1 < x2 :
    maiornum = "x2"
    
elif x3 > x1 :
    maiornum = "x3"
print("O maior número é {}".format(maiornum))
