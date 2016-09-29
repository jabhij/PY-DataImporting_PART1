"""
Instructions --

- Complete the argument of create_engine() so that the engine for the SQLite database 'Chinook.sqlite' is created.
- Execute the query that selects all records from the Employee table where 'EmployeeId' is greater than or equal to 6. Use the >= operator and assign the results to rs.
- Apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
- Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.
"""

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT * from Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())
