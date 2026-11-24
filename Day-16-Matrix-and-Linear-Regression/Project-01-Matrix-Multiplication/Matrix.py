#building a small program using numpy which calculates two matrix
import numpy as np

A = (
    [
        [1,2],
        [3,4]
    ]
)


B = (
    [
        [5,6],
        [7,8]
    ]
)

c = np.matmul(A,B)

print("Result:",c)