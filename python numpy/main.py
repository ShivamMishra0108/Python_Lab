import numpy as np

a = np.array([1,2])

print(a)

ab = np.arange(1,11)
print(ab)

ac = np.arange(0,30,3) # low, high, common difference
print(ac)

ax = np.arange(1,11).reshape(5,2)
print(ax)

x = np.ones((3,4))
y = np.zeros((3,4))
z = np.random.random((3,4))

print(x)
print(y)
print(z)

ad = np.linspace(-10,10,10,dtype=int)   # low range,/ high range,/ no of elements,/  default(float)

ae = np.identity(3) # diagonal matrix

print(ad)
print(ae)



# ndim :   no of dimanesions
# shape:   no of row, column
# size:    no of elements
# itemsoze:  space occupied in bits

print(x.ndim)
print(z.shape)
print(y.size)
print(x.itemsize)

# dtype:  Datatype

print(a.dtype)
print(y.dtype)
print(ad.dtype)

# astype: change datatype

a.astype(np.int32)
y.astype(np.int32)


print(a.dtype)
print(y.dtype)
print(ad.dtype)

