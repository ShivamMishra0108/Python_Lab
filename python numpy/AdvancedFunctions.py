import numpy as np

# SIGMOID FUNCTION 

def sigmoid(array):
    return 1/(1 +np.exp(-(array)))

a = np.arange(10)
print(sigmoid(a))

#  MEAN SQUARED ERROR

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

def mse(actual,predicted):
    return np.mean((actual-predicted)**2)

print(mse(actual,predicted))


# WORKING WITH MISSING VALUE:   NP.NAN

a1 = np.array([1,2,3,4,np.nan,np.nan,5,])

print(np.isnan(a1))

