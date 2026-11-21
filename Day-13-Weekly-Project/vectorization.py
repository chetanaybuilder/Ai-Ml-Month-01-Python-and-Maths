#importing required libraries
import numpy as np
import time

#creating a dataset
numbers = list(range(1,1000001)) 
np_numbers = np.array(numbers)


#python loop benchmark
start_time = time.perf_counter()

result_addition = []
for number in numbers:
   result_addition.append(number * 2)

end_time = time.perf_counter()

python_time = end_time - start_time



#numpy vectorized benchmark
start_time = time.perf_counter()

numbers_add = np_numbers * 2

end_time = time.perf_counter()

numpy_time = end_time - start_time


#calculate speedup
speedup = python_time/numpy_time


#displaying result
print("python loop time:",python_time)
print("numpy vectorization time:",numpy_time)
print("speedup:",speedup,"x")




