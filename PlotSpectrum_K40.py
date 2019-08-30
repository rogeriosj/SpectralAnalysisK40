import math
import numpy as np
import matplotlib.pyplot as plt

# Load data
f = open('AmostraK40_2019.txt')
# skip first 27 header lines
for i in range(27):
    header = f.readline()

# now load data
x = []
y = []
for line in f:
    line = line.strip()
    columns = line.split()
    if(float(columns[2])>0):
        x.append(float(columns[1]))
        y.append(math.log(float(columns[2])))
    print(columns[1], columns[2])


# Graphical parameters
colors = ( 0 , 0 , 0 )
area   = np.pi*3

# Plot
plt.scatter( x, y, s=area, c=colors, alpha=0.5)
plt.xlabel('E[KeV]')
plt.ylabel('Counts')
plt.savefig("PlotSpectrum_K40.jpg")
