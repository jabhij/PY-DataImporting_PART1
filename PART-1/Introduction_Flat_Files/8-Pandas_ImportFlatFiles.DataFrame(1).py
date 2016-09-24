"""
Instructions --

- Import the pandas package using the alias pd.
- Read titanic.csv into a DataFrame called df. The file is already stored in the file object.
- In a print() call, view the head of the DataFrame.
"""

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())
