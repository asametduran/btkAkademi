import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[4]

result = numbers[-1]

result = numbers[3:6]

result = numbers[::]

result = numbers[::-2]

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])

result = numbers2[0]

result = numbers2[2]

result = numbers2[0,2]

result = numbers2[:,0]

result = numbers2[:,0:2]

result = numbers2[-1,:]

result = numbers2[:2,:2]

arr1 = np.arange(0,10)
arr2 = arr1
print(arr1)
print(arr2)

arr2[0] = 20

print(arr1)
print(arr2)

arr2 = arr1.copy()

print(arr1)
print(arr2)

# print (numbers2)

# print (result)