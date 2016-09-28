"""
Instructions --

- Import the function create_engine from the module sqlalchemy.
- Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to engine.
- Using the method table_names() on the engine engine, assign the table names of 'Chinook.sqlite' to the variable table_names.
- Print the object table_names to the shell.
"""

# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)
