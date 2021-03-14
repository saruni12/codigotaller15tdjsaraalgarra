import numpy as np


x = np.array([0, 2, 3, 6,7])


y = np.array([0.120,0.153,0.170,0.225,0.260])

coeffs = np.polyfit(x,y,1)
b1 = coeffs[0]
b0 = coeffs[1]
estimar_y = b0 + (b1 * x)
print(b0)
print(b1)

