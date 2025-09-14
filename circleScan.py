'''
The actual scan for a circle of each radius.
'''

import numpy as np
from time import time

start = time()

xfunc = np.linspace(0, 1, 10000000)
xPoints = np.linspace(0.666817, 0.666917, 100, dtype = 'd') # x-points to be scanned
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

def findLowestMag(iPoint, yPoints, index): # iPoint is the point that you are finding the closest line point to
                                           # yPoints is the list of y-values in the curve, index is where to start
    # Defining immediate variables
    counter = 0
    smallestMag = 100

    for i in range((len(yPoints)) - index): # Range of points to search
        vectorMag = pointMag(xfunc[index + i], yPoints[index + i], iPoint, 0) # Circle centered on x-axis, y always 0
        if vectorMag < smallestMag:
            smallestMag = vectorMag
        else:
            continue
        counter += 1

    return smallestMag, counter

# Write output of curves to array of y-values
curveAiter = (x**2 for x in xfunc)
curveBiter = (x**2 - 1 for x in xfunc)
curveAOutput = np.fromiter(curveAiter, dtype = 'd')
curveBOutput = np.fromiter(curveBiter, dtype = 'd')

# Start scan to find the closest point on each curve; if they are equal, that might actually just be it...
smallestMagA, smallestMagB = 100, 100 # Define smallest magnitude that is not real
indexA, indexB = 0, 0 # Initial index
xPointsIndex = 0 # DEBUG
print('debug') # debug
for xCenter in xPoints:
    smallestMagA, indexA = findLowestMag(xCenter, curveAOutput, indexA)
    smallestMagB, indexB = findLowestMag(xCenter, curveBOutput, indexB)
    xPointsIndex += 1
    print(str(round(xPointsIndex/len(xPoints) * 100, 3)) + '% ' + '(' + str(xPointsIndex) + '/' + str(len(xPoints)) + ')', flush = True)
    if np.allclose(smallestMagA, smallestMagB):
        break
    else:
        continue
print(smallestMagA, indexA)
print(smallestMagB, indexB)
print(xPoints[xPointsIndex])

end = time()

print(str(round(end - start, 3)) + ' seconds')