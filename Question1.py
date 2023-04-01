# a. Using NumPy create random vector of size 15 having only Integers in the range 1-20.
# 1. Reshape the array to 3 by 5
# 2. Print array shape.
# 3. Replace the max in each row by 0

import numpy as np
#randint method to create random numbers with range 1-20 of size 15
arr = np.random.randint(20,size=(15))
print("array of random numbers from range 1 to 20:")
print(arr)
x=arr.reshape(3,5)
print("after reshape:")
print(x)
print("shape: ",x.shape)
print("max number in all rows changed to 0:")
#returning array of max values in every horizontal axis row
max1 = x.max(axis=1).reshape(-1, 1)
#changing max values to 0 and keeping other values undisturbed
res = np.where(x == max1, 0,x)
print(res)


