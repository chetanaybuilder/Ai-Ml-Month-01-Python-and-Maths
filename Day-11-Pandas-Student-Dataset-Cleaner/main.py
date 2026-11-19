#importing the required library
import pandas as pd


#reading the csv file
df = pd.read_csv("data/messy_student.csv")


#cleaning csv data
df["Name"] = df["Name"].str.strip()
df["Class"] = df["Class"].str.strip()

df = df.drop_duplicates()

for column in ["Marks", "Attendance"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")
    df.loc[~df[column].between(0, 100), column] = pd.NA
    df[column] = df[column].fillna(df[column].mean()).round().astype(int)

print(df)


#performing operations on csv data
result = df.groupby("Class")["Marks"].agg(
    [
    "mean","max","min","sum"
]
)


#printing the result
print(result)



#exporting clean csv
df = df.sort_values(by="Student_ID")
df.to_csv("cleaned_student.csv", index=False)
print("cleaned dataset saved sucessfully!")
