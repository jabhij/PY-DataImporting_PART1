"""
Instructions --

- Open the engine connection as con using the method connect() on the engine.
- Execute the query that selects ALL columns from the Album table. Store the results in rs.
- Store all of your query results in the DataFrame df by applying the fetchall() method to the results rs.
- Close the connection!
"""

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute('SELECT * from Album')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())
