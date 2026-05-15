import numpy as np

a = np.arange(27).reshape(3,3,3)

# Fancy Indexing
print(a[:,[0,2]])


# Boolean Indexing:

a = np.random.randint(1,100,24).reshape(6,4)

print(a,"\n")

print(a[a>50])

print(a[a%2 == 0])

print(a[(a>50) & (a%2 == 0)])