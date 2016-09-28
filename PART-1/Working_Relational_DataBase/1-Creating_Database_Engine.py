"""
Instructions --

- Import the function create_engine from the module sqlalchemy.
- Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to engine.
"""

# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
