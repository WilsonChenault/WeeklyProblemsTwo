import numpy as np

def curveA(x):
    y = x**2
    return y

def curveB(x):
    y = x**2 - 1
    return y

def tangent(x, y): #  Only need one function because each curve has the same derivative
    slope = 2*x
    return slope, x, y

# Write code to create a file each that contains all the points of each curve with a resolution of 1*10^-6
xPoints = np.linspace(0, 1, 1000000)
with open('curveA.txt', 'w') as f: # Point on each line for curve A
    for i in xPoints:
        f.write(str(i)+ ', ' + str(curveA(i)) + '\n')
    f.close()
with open('curveB.txt', 'w') as g: # Point on each line for curve B
    for i in xPoints:
        g.write(str(i) + ', ' + str(curveB(i)) + '\n')
    g.close()

# Feeding the points through to find the tangent lines at each point and storing those in a file
with open('curveA.txt', 'r') as f: # file for tangent lines of curve A
    with open('tangentsA.txt', 'w') as g:
        for line in f:
            line = line.split(', ')
            slope, x, y = tangent(float(line[0]), float(line[1]))
            g.write(str(x) + ', ' + str(y) + ', ' + str(slope) + '\n') # IMPORTANT: STORED AS (X, Y, SLOPE) not usual
        g.close()
    f.close()
with open('curveB.txt', 'r') as f: # file for tangent lines of curve B
    with open('tangentsB.txt', 'w') as g:
        for line in f:
            line = line.split(', ')
            slope, x, y = tangent(float(line[0]), float(line[1]))
            g.write(str(x) + ', ' + str(y) + ', ' + str(slope) + '\n') # IMPORTANT: STORED AS (X, Y, SLOPE) not usual
        g.close()
    f.close()