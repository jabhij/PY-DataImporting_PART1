"""
Instructions --

- Assign the filename to the variable file.
- Pass the correct argument to pd.ExcelFile() to load the file using pandas.
- Print the sheetnames of the Excel spreadsheet by passing the necessary argument to the print() function.
"""

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
