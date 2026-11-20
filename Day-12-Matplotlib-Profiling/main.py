#importing reqiured library
import matplotlib.pyplot as plt
import cProfile
import timeit
import pstats


# Read data
subjects = []
marks = []

with open("data/data.txt", "r") as file:
    for line in file:
        subject, mark = line.strip().split(",")

        subjects.append(subject)
        marks.append(int(mark))


# Create chart
fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(subjects, marks)

ax.set_title("Student Performance")
ax.set_xlabel("Subjects")
ax.set_ylabel("Marks")

fig.tight_layout()
fig.savefig("chart.png", dpi=300)

plt.show()


# Profile the program
profiler = cProfile.Profile()

profiler.enable()

# Example operation to profile
total = sum(marks)

profiler.disable()


# Save profiling report
stats = pstats.Stats(profiler)

stats.sort_stats("cumulative")
stats.dump_stats("profile.prof")


# Benchmark
execution_time = timeit.timeit(
    lambda: sum(marks),
    number=1000
)

print("Total:", total)
print("Execution time:", execution_time)