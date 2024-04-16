import pandas as pd
import numpy as np

# Import DataFrame
df = pd.read_csv('sales_data.csv', sep=";")

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in the dataset:\n", missing_values)

# Drop rows with missing values (if necessary)
# df = df.dropna()

# Format Date
print("Start Processing ...")
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['month-year'] = df['date'].dt.strftime('%m-%Y')  # Simplified date formatting

# Create a pivot table for easier manipulation
pivot_table = pd.pivot_table(df, values='sales', index=['store', 'item'],
                             columns=['month-year'], aggfunc=np.sum, fill_value=0)

# Sort by store and item
pivot_table.sort_index(inplace=True)

print("Processing is completed.")
print("{:,} lines in your final report".format(len(pivot_table)))

# Define the order of columns in the final report
# You may want to customize this based on specific requirements
my_cols = [f"{month:02d}-{year}" for year in range(2013, 2018) for month in range(1, 13)]

# Reorder columns based on defined order
pivot_table = pivot_table[my_cols]

# Final report
print("Start saving report.")
pivot_table.to_excel('sales_report.xlsx')
print("Your report is saved.")