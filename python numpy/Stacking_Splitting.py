import numpy as np

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12).reshape(3,4)

a3 = np.hstack(a2)
a4 = np.vstack(a1,a2,a1)

print(a3)
print(a4)

print(np.vsplit(a3))
np.hsplit(a4)