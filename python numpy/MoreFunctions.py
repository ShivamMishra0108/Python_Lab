import numpy as np

a = np.random.randint(1,100,24).reshape(6,4)
b = np.array([1,4,5,6,7,5,3,34,5,6,7,8,])


# ADD A COLUMN TO MATRIX:

print(np.append(a,np.ones((a.shape[0],1)),axis=1))


# ADD A ROW TO MATRIX:

print(np.append(a,np.ones((1,a.shape[1])),axis=0))

print(np.append(a,np.random.random((a.shape[0],1)),axis=1))

# CONCATENATE

c = np.arange(0,6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)

print(np.concatenate((c,d),axis=0))
print(np.concatenate((c,d),axis=1))


# UNIQUE

#np.unique()


# Expand Dimensions of array,/ Matrix:

print(np.expand_dims(c,axis=0))
print(np.expand_dims(c,axis=1))

# np.where:  USED TO RETURN OR OPERATE ON THE INDEX OF THE ELEMENTS GIVEN IN THE CONDITION:

print(np.where(b>6))

print(np.where(b>6,0,b))

# argmax/argmin:  Return the index of the maximum or minimum element 

print(np.argmax(b))

print(np.argmin(a,axis=0))


#ISIN

items = ([10,20,30,40,50,60])
print(np.isin(b,items))

# FLIP:   Bascially Reverses the array

np.flip(b)
np.flip(a,axis=1)
np.flip(a,axis=0)


#PUT: Permanently change the value of element 

np.put(b,[0,1],[20,30])

#DELETE: Deletes the element from the given index

np.delete(b,0)