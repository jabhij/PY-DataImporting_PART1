"""
Instructions --

- Execute the SQL query that selects the columns LastName and Title from the Employee table. Store the results in the variable rs.
- Apply the method fetchmany() to rs in order to retrieve 3 of the records. Store them in the DataFrame df.
- Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.
"""

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title from Employee')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())
