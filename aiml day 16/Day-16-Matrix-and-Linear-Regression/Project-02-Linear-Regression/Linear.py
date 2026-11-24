#creating A small linear regression model using numpy
import numpy as np

X = np.array([

    [500],
    [700],
    [900],
    [1100],
    [1300]

])


y = np.array([25,35,45,55,65])


X = np.column_stack((np.ones(len(X)),X))


theta = np.linalg.solve(
    X.T @ X, 
    X.T @ y
)

predictions = X @ theta

print("Learned parameters:",theta)
print("Predictions:",predictions)


new_house = np.array([[1 , 1000]])

prediction = new_house @ theta


print("Predicted price:")
print(prediction[0],"Lakh")



errors = y - predictions

squared_errors = errors ** 2

total_error = np.sum(squared_errors)

print("Total error:",total_error)
