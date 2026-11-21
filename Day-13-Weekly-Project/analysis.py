#importing required libraries
import pandas as pd


#pandas reading the csv file
df = pd.read_csv("data/dataset.csv")


#checking data dimensions
df.shape 


#checking columns
df.columns


#checking datatype
df.dtypes


#checking missing values
df.isnull().sum()


#checking duplicated values
df.duplicated().sum()


#generating statistical summary
df.describe()


#removing whitespaces
df["Product"] = df["Product"].str.strip()


#converting values into datetime format
df["Date"] = pd.to_datetime(df["Date"])


#using groupby to get total revenue
df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)


#using .agg() to perform multiple operation
df.groupby("Product")["Revenue"].agg(["sum","mean","max","min"])