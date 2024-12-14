import numpy as np 

matrix1 = np.array([[1,2],[3,4]])
matrix2=np.array([[1,2],[3,4]])

print(f"matrix1:\n{matrix1}")
print(f"matrix2:\n{matrix2}")

sum =matrix1+matrix2
print(f"sum:\n{sum}")
multiply = np.dot(matrix1,matrix2)
print(f"multiply:\n{multiply}")