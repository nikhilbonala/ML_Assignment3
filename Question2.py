#  2-dimensional array of size 4 x 3
import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,1]], np.int32)
print(type(x))
print(x.shape)
print(x.dtype)

# B. program to compute the eigenvalues and right eigenvectors of a given square array given below

arr = np.array([[3, -2],[1, 0]])
#using eig method from linear algebra (linalg)
values, vectors = np.linalg.eig(arr)
print("Eigen values: ",values)
print("Right eigenvectors :",vectors)

# C. sum of the diagonal element of a given array

arr1 = np.arange(6).reshape(2,3)
result =  np.trace(arr1)
print("Sum of the diagonal element in given matrix:")
print(result)

# D. Write a NumPy program to create a new shape to an array without changing its data

a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(3,2)
print("Reshape to 3x2:",b)
c = a.reshape(2,3)
print("Reshape to 2x3:",c)
