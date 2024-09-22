# This program uses matplotlib to graphically get two points.

import matplotlib.pyplot as plt

plt.axis([-4, 4, -3, 3])
plt.axis("equal")
plt.grid("on")
plt.title("Choose 2 points!")
p1, p2 = plt.ginput(2)

# extract coords from points
x1, y1 = p1
x2, y2 = p2

print("Point1:", p1)
print("Point2:", p2)

# Compute and print the distance between the points!
import math
distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print("A distancia entre P1 e P2 é :{}".format(distance))

