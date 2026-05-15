import sys
import time

import numpy as np

# TIME

a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c= []

start = time.time()
for i in range(len(a)):
    c.append(a[i]+b[i])
print(time.time()-start)


x = np.arange(10000000)
y = np.arange(10000000,20000000)

start = time.time()
z = x+y
print(time.time()-start)

# MEMORY

print(sys.getsizeof(a))
print(sys.getsizeof(x))


# CONVIENIENCE: Its easy to operate on numpy functions as compared to python