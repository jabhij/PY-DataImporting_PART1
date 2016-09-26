"""
Instructions --

- Parse the first sheet by index. In doing so, skip the first row of data, then name the columns 'Country' and 'AAM due to War (2002)' by 
using the argument names. The arguments passed to skiprows and names will all need to be of type list.
- Parse the second sheet by index. In doing so, parse only the first column with the parse_cols parameter, skip the first row and rename 
the column 'Country'. The argument passed to parse_cols will need to be of type list.
"""

# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())
 
