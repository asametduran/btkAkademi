import numpy as np

np_array = np.array([1,3,5,7,9])

result = np.arange(1,10)

result = np.arange(10,100,3)

result = np.zeros((5,5))

result = np.ones(10)

result = np.linspace(0,100,5)

result = np.linspace(0,5,5)

result = np.random.randint(0,10)

result = np.random.randint(20)

result = np.random.randint(0,10,3)

result = np.random.randn(5)

result = np.arange(50).reshape(5,10)

print (result.sum(axis=1))

print (result.sum(axis=0))

result = np.random.randint(1,100,10)

result = result.max()
result = result.min()
result = result.mean()
result = result.argmax()
result = result.argmin()

print (result)