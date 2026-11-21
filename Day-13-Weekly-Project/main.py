#importing required libraries
import analysis
import vectorization
import visualization


#printin everything
print("========== DATA ANALYSIS REPORT ==========")

print("\nDataset Preview:")
print(analysis.df.head())

print("\nDataset Shape:")
print(analysis.df.shape)

print("\nMissing Values:")
print(analysis.df.isnull().sum())

print("\nRevenue Analysis:")
print(
    analysis.df.groupby("Product")["Revenue"]
    .agg(["sum", "mean", "max", "min"])
)

print("\n========== REPORT COMPLETED ==========")