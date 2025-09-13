'''
The actual scan for a circle of each radius.
'''

import numpy as np
from time import time

start = time()

xPoints = np.linspace(0.64, 0.68, 1000) # x-points to be scanned
print(xPoints) # DEBUG

def pointMag(x1, y1, x2, y2):
    xMag = abs(x2 - x1)
    yMag = abs(y2 - y1)
    magnitude = np.sqrt(xMag**2 + yMag**2)
    return magnitude

def findLowestMag(fileA, fileB):
    counter = 0
    with open(fileA, 'r') as file, open(fileB, 'w') as log:
        for line in file:
            line = line.split(', ')
            vectorMag = round(pointMag(float(line[0]), float(line[1]), xCenter, 0), 7)  # y2 always 0, centered on x-axis
            if vectorMag < smallestMagA:  # Keep smallest vectorMag that has been found;
                smallestMagA = vectorMag
            elif vectorMag == smallestMagA: # if equal no one cares
                continue
            elif vectorMag > smallestMagA: # Break loop if the magnitude ever increases
                break
            counter += 1  # DEBUG
            log.write(str(vectorMag) + ', ' + str(counter) + ', ' + str(xCenter) + '\n')  # DEBUG

# Start scan to find the closest point on each curve; if they are equal, that might actually just be it...
smallestMagA = 100 # Define smallest magnitude that is not real
smallestMagB = 100 # Define smallest magnitude that is not real
counterA = 0 # DEBUG
counterB = 0 # DEBUG
with (open('curveA.txt', 'r') as fileA, open('curveB.txt', 'r') as fileB,
      open('magnitudesA.txt', 'w') as fileC, open('magnitudesB.txt', 'w') as fileD):
    for xCenter in xPoints:
        for line in fileA:
            line = line.split(', ')
            vectorMag = round(pointMag(float(line[0]), float(line[1]), xCenter, 0), 7) # y2 always 0, centered on x-axis
            if vectorMag < smallestMagA: # Keep smallest vectorMag that has been found;
                smallestMagA = vectorMag
            elif vectorMag == smallestMagA:
                continue
            elif vectorMag > smallestMagA:
                break
            counterA += 1 # DEBUG
            fileC.write(str(vectorMag) + ', ' + str(counterA) + ', ' + str(xCenter) + '\n') # DEBUG
        for line in fileB:
            line = line.split(', ')
            vectorMag = round(pointMag(float(line[0]), float(line[1]), xCenter, 0), 7) # y2 always 0, centered on x-axis
            if vectorMag < smallestMagB:
                smallestMagB = vectorMag
            elif vectorMag == smallestMagB:
                continue
            elif vectorMag > smallestMagB:
                break
            counterB += 1 # DEBUG
            fileD.write(str(vectorMag) + ', ' + str(counterB) + ', ' + str(xCenter) + '\n') # DEBUG
        if smallestMagA == smallestMagB:
            break
        else:
            continue
    fileA.close()
    fileB.close()
print(smallestMagA, counterA)
print(smallestMagB, counterB)

end = time()

print(str(round(end - start, 3)) + ' seconds')