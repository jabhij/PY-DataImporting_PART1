### Work Flow of SQL Querying using Python

Let's go through the workflow in these six easy steps--

- Import Pakcages and Functions   
**`from sqlalchemy import create_engine`**

- Create the DataBase Engine   
**`import pandas as pd`**

- Connect to the Engine   
**`engine = create_engine('sqlite:///Database_Name.sqlite')`**

- Query the Database   
**`con = engine.connect()`**

- Save Query Results to a DataFrame   
**`rs = con.execute("SELECT * from Table_Name")`**

- Close the Connection   
**`df = pd.DataFrame(rs.fetchall())`**

As simple as that.
