'''
The actual scan for a circle of each radius.
'''

import numpy as np
from time import time

start = time()

xfunc = np.linspace(0, 1, 100000)
xPoints = np.linspace(0.64, 0.68, 1000) # x-points to be scanned
print(xPoints) # DEBUG

def curveA(x):
    y = x**2
    return y

def curveB(x):
    y = x**2 - 1
    return y

def pointMag(x1, y1, x2, y2):
    xMag = abs(x2 - x1)
    yMag = abs(y2 - y1)
    magnitude = np.sqrt(xMag**2 + yMag**2)
    return magnitude

def findLowestMag(fileA, fileB, index):
    counter = 0
    smallestMag = 100
    with open(fileA, 'r') as file, open(fileB, 'w') as log:
        for line in file:
            line = line.split(', ')
            vectorMag = round(pointMag(float(line[0]), float(line[1]), xCenter, 0), 7)  # y2 always 0, centered on x-axis
            if vectorMag < smallestMagA:  # Keep smallest vectorMag that has been found;
                smallestMagA = vectorMag
            elif vectorMag >= smallestMagA: # Break loop if the magnitude ever increases
                break
            counter += 1  # DEBUG
            log.write(str(vectorMag) + ', ' + str(counter) + ', ' + str(xCenter) + '\n')  # DEBUG
    return smallestMag, counter

# Write output of curves to array of y-values
curveA = (x**2 for x in xfunc)
curveB = (x**2 - 1 for x in xfunc)
curveAOutput = np.fromiter(curveA, dtype = 'd')
curveBOutput = np.fromiter(curveB, dtype = 'd')

# Start scan to find the closest point on each curve; if they are equal, that might actually just be it...
smallestMagA, smallestMagB = 100, 100 # Define smallest magnitude that is not real
indexA, indexB = 0, 0 # Initial index
for xCenter in xPoints:
    smallestMagA, indexA = findLowestMag('curveA.txt', 'magnitudesA.txt', indexA)
    smallestMagB, indexB = findLowestMag('curveB.txt', 'magnitudesB.txt', indexB)
    if np.allclose(smallestMagA, smallestMagB):
        break
    else:
        continue
print(smallestMagA, indexA)
print(smallestMagB, indexB)

end = time()

print(str(round(end - start, 3)) + ' seconds')
