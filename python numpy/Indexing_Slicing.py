import numpy as np

a1 = np.array([1,2,3,4,5,6,7,8,9])

a2 = np.arange(1,13).reshape(3,4)
print(a1)
print(a2)

print(a1[0])
print(a1[-1])

print(a1[2:5])

print(a2[1,:])
print(a2[:,0])

print(a2[1:,1:3])

print(a2[::2,::3])

print(a2[0::2,1::2],"\n")


print(a2[0:2,1:])

a3 = np.arange(27).reshape(3,3,3)
print(a3)

print(a3[0,1,0:])



