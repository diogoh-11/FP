lst = [(7, "corpos"), (2, "dlma"), (2,"copo") , (7,"maoses") ]    # a list of pairs



lst2 = sorted(lst, key=lambda t: len(t[1]) )

print(lst2)