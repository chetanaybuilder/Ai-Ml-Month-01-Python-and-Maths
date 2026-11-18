#importing required libraries
import numpy as np
import time


# Build equivalent source data for the native Python and NumPy benchmarks.
start_time = time.perf_counter()
numbers = list(range(1, 1_000_001))
python_dataset_time = time.perf_counter() - start_time


# Measure the one-time conversion cost separately from the operations below.
start_time = time.perf_counter()
arr = np.array(numbers)
numpy_dataset_time = time.perf_counter() - start_time


# Python addition: apply a scalar increment to each list element.
start_time = time.perf_counter()
python_addition_result = []
for number in numbers:
    python_addition_result.append(number + 10)
python_addition_time = time.perf_counter() - start_time


# NumPy addition: broadcast the increment across the entire array.
start_time = time.perf_counter()
numpy_addition_result = arr + 10
numpy_addition_time = time.perf_counter() - start_time


# Python multiplication: scale each list element with a native loop.
start_time = time.perf_counter()
python_multiplication_result = []
for number in numbers:
    python_multiplication_result.append(number * 2)
python_multiplication_time = time.perf_counter() - start_time


# NumPy multiplication: scale all array elements using vectorized arithmetic.
start_time = time.perf_counter()
numpy_multiplication_result = arr * 2
numpy_multiplication_time = time.perf_counter() - start_time


# Python squaring: calculate each element's square with a native loop.
start_time = time.perf_counter()
python_squaring_result = []
for number in numbers:
    python_squaring_result.append(number ** 2)
python_squaring_time = time.perf_counter() - start_time


# NumPy squaring: calculate every square through vectorized exponentiation.
start_time = time.perf_counter()
numpy_squaring_result = arr ** 2
numpy_squaring_time = time.perf_counter() - start_time


# Python filtering: retain list values greater than the shared threshold.
start_time = time.perf_counter()
python_filtering_result = []
for number in numbers:
    if number > 50:
        python_filtering_result.append(number)
python_filtering_time = time.perf_counter() - start_time


# NumPy filtering: build a Boolean mask for values above the threshold.
start_time = time.perf_counter()
numpy_filtering_result = arr > 50
numpy_filtering_time = time.perf_counter() - start_time


# Python summation: accumulate list values one at a time.
start_time = time.perf_counter()
total = 0
for number in numbers:
    total += number
python_sum_time = time.perf_counter() - start_time


# NumPy summation: reduce the array to a single aggregate value.
start_time = time.perf_counter()
numpy_sum_result = np.sum(arr)
numpy_sum_time = time.perf_counter() - start_time


# Keep setup measurements visible, but separate from the computation total.
timings = [
    ("Dataset creation", python_dataset_time, numpy_dataset_time),
    ("Addition", python_addition_time, numpy_addition_time),
    ("Multiplication", python_multiplication_time, numpy_multiplication_time),
    ("Squaring", python_squaring_time, numpy_squaring_time),
    ("Filtering", python_filtering_time, numpy_filtering_time),
    ("Summation", python_sum_time, numpy_sum_time),
]

print("\n" + "=" * 68)
print("                 PYTHON vs NUMPY PERFORMANCE")
print("=" * 68)
print("{:<22} {:>14} {:>14} {:>14}".format(
    "Operation", "Python (s)", "NumPy (s)", "Faster"
))
print("-" * 68)

for operation, python_time, numpy_time in timings:
    faster = "Python" if python_time < numpy_time else "NumPy"
    print("{:<22} {:>14.6f} {:>14.6f} {:>14}".format(
        operation, python_time, numpy_time, faster
    ))

# Compare operation time only; list and array setup are not equivalent work.
python_total_time = sum((
    python_addition_time,
    python_multiplication_time,
    python_squaring_time,
    python_filtering_time,
    python_sum_time,
))
numpy_total_time = sum((
    numpy_addition_time,
    numpy_multiplication_time,
    numpy_squaring_time,
    numpy_filtering_time,
    numpy_sum_time,
))

print("-" * 68)
print("{:<22} {:>14.6f} {:>14.6f}".format(
    "Total computation", python_total_time, numpy_total_time
))

if python_total_time < numpy_total_time:
    overall_winner = "Python"
    speedup = numpy_total_time / python_total_time
else:
    overall_winner = "NumPy"
    speedup = python_total_time / numpy_total_time

print("\nOverall winner: {} ({:.2f}x faster for computation)".format(
    overall_winner, speedup
))
print("=" * 68)
