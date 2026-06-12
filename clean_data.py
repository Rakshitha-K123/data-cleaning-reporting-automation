import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("messy_data.xlsx")

print("Original Data")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(round(df["Age"].mean(), 0))

# Fill missing Salary with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Standardize text
df["Name"] = df["Name"].str.title()
df["City"] = df["City"].str.title()

df = df.drop_duplicates()

# Save cleaned data
df.to_excel("cleaned_data.xlsx", index=False)

# Create summary report
report = f"""
Total Records: {len(df)}

Average Age: {df['Age'].mean():.2f}

Average Salary: {df['Salary'].mean():.2f}
"""

with open("summary_report.txt", "w") as f:
    f.write(report)

# Create chart
city_counts = df["City"].value_counts()

plt.bar(city_counts.index, city_counts.values)

plt.title("Employees by City")

plt.xlabel("City")

plt.ylabel("Count")

plt.savefig("data_summary.png")

plt.show()

print("Cleaning Completed!")