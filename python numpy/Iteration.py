import numpy as np

a3 = np.arange(27).reshape(3,3,3)

for i in a3:
    print(i)

for i in np.nditer(a3):
    print(i)


    