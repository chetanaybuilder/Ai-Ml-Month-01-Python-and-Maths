#importing required libraries
import matplotlib.pyplot as plt
import analysis
import vectorization

# Group revenue by product
revenue_by_product = analysis.df.groupby("Product")["Revenue"].sum()

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

#Create bar chart
ax.bar(
    revenue_by_product.index,
    revenue_by_product.values
)

#Add chart labels and title
ax.set_title("Revenue by Product")
ax.set_xlabel("Product")
ax.set_ylabel("Total Revenue")

#Rotate x-axis labels if needed
plt.xticks(rotation=45)

#Adjust layout
plt.tight_layout()

#Display chart
plt.savefig("charts/revenue_by_product.png")
plt.show()

#Benchmark comparison
labels = ["Python Loop", "NumPy Vectorization"]
times = [vectorization.python_time, vectorization.numpy_time]

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(labels, times)

ax.set_title("Python vs NumPy Execution Time")
ax.set_xlabel("Method")
ax.set_ylabel("Execution Time (seconds)")

plt.tight_layout()
plt.savefig("charts/vectorization_benchmark.png")
plt.show()