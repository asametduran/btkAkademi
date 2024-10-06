import pandas as pd
import numpy as np

#data
numbers = [20,30,40,50]
letters = ['a', 'b', 'c', 'd', 'e', 20]
scalar = 5
dict = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
random_numbers = np.random.randint(10,100,6)

# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(5,[0,1,2,3])
# pandas_series = pd.Series(numbers,['a', 'b', 'c', 'd', 'e'])
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(dict)
pandas_series = pd.Series(random_numbers)

result = pandas_series[0]

print(pandas_series)
print (result)
print (pandas_series[0])
print (pandas_series[:-1])
print (pandas_series[:2])
print(pandas_series['a'])