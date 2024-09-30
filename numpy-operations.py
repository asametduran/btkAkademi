import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
result = numbers1 + numbers2 + 10
result = numbers1 - numbers2 
result = numbers1 * numbers2
result = numbers1 / numbers2
result = numbers1 % numbers2
result = np.sin(numbers1) #sin()
result = np.cos(numbers1) #cos()
result = np.sqrt(numbers1) #sqrt()
result = np.log(numbers1) #log()

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

result = np.vstack((mnumbers1,mnumbers2)) #vstack

result = np.hstack((mnumbers1,mnumbers2)) #hstack

result = numbers1 >= 50
result = numbers1 % 2 == 0

print (numbers1[result])

print(result)