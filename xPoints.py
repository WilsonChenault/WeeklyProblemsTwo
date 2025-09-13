import numpy as np

x = 0.6
with open('xPoints.txt', 'w') as f:
    while x <= 0.7:
        f.write(str(x) + '\n')
        x += 0.0000001