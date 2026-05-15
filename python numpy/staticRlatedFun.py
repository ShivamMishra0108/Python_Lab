import numpy as np

a = np.random.randint(1,100,24).reshape(6,4)
b = np.array([1,4,5,6,7,5,3,20,34,5,6,40,7,8,])


# CUMSUM/CUMPROD:   Consecutive sum or product every element

print(np.cumsum(b))

print(np.cumprod(b))

#percentile: percentile of n before the nth percentile:

print(np.percentile(b,50))


# HISOGRAM: Represants frequency of data present in the given bin size:

print(np.histogram(b,bins=[0,10,20,30,40]))


# corrcioef: Represents corelation between two arrays,etc

#np.corrcoef(a,b)


