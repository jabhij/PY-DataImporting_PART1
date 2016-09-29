"""
Instructions --

- Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
- In the context manager, execute the query that selects all records from the Employee table and orders them in increasing order by the 
column BirthDate. Assign the result to rs.
- In a call to pd.DataFrame(), apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
- Set the DataFrame's column names to the corresponding names of the table columns.
"""

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * from Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())
