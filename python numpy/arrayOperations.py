import numpy as np

a1 = np.arange(12).reshape((3,4))
a1 = a1*100
print(a1)
a1.astype(int)


#  mathematical: max/min/sum/prod etc

print(np.max(a1))
print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))

# 0 -> col,  1-> row

print(np.max(a1,axis=0))
print(np.max(a1,axis=1))


# statistic:  meean/median/standard deviatin etc

print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))

# Trigonometric funcrions

np.sin(a1)

# Dot product

a2 = np.arange(12,24).reshape(4,3)
print(np.dot(a1,a2))

# log and exponents functions

np.log(a1)
np.exp(a1)

# ROUND FIGURES:  round/floor/ceil