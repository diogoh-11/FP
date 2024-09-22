lstA = [1, 2, 3, 4, 5]
lstB = [6, 7, 8, 9, 10]
print(lstA[-2])
print(lstA[2]+lstB[1])
print(len(3*lstA))
lstC = 2*lstA[1::3] + lstB[:2]
for i in lstC:
    print(i, end=',')
print()