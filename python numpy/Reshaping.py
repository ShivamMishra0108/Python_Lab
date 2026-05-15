import numpy as np

# reshape
# Transpose
# Ravel: Makes any array 1D

a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

print(a2)
print(np.transpose(a2))
# OR
a2.T

print(a3.ravel())

