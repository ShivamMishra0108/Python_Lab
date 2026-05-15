import numpy as np

a2 = np.arange(1,13).reshape(3,4)
print(a2)

#scaler operations:
print(a2*2)
print(a2**2)

# relational operations
print(a2>10)

# vector operations
a1 = np.ones((3,4))
print(a2+a1)

