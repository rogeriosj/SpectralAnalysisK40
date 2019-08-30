import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

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

def lin_func(x, a, b):
    return a * x + b

v_lin_func = np.vectorize(lin_func)

params, params_cov = optimize.curve_fit(lin_func, x, y)

print(params) 

y_fit = v_lin_func(x, params[0], params[1])
print(y_fit)

# Plot
plt.scatter( x, y, s=area, c=colors, alpha=0.5)
plt.scatter(x,y_fit)
plt.xlabel('E[KeV]')
plt.ylabel('Counts')
#plt.axis([930,970,10,11])
#plt.savefig("PlotSpectrum_K40.jpg")
plt.show()

