import numpy as np

a = np.random.randint(1,100,24).reshape(6,4)

print(np.sort(a),"\n")

print(a,"\n")

print(np.sort(a,axis=1),"\n")
print(np.sort(a,axis=0),"\n")

b = np.array([1,4,5,6,7,5,3,34,5,6,7,8,])

print(np.sort(b))

# DESCENDING ORDER:

print(np.sort(a,axis=1)[:,::-1])

print(np.sort(b)[::-1])


