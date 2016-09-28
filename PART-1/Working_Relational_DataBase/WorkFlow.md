## Work Flow of SQL Querying using Python

### 1: Traditional Approach

Let's go through the workflow in these six easy steps--

- Import Pakcages and Functions   
**`from sqlalchemy import create_engine`**

- Create the DataBase Engine   
**`import pandas as pd`**

- Connect to the Engine   
**`engine = create_engine('sqlite:///Database_Name.sqlite')`**   
**`con = engine.connect()`**

- Query the Database   
**`rs = con.execute("SELECT * from Table_Name")`**

- Save Query Results to a DataFrame   
**`df = pd.DataFrame(rs.fetchall())`**   
**`df.colums = rs.keys()`**

- Close the Connection   
**`con.close()`**

As simple as that.

### 2: 'Context Manager' Approach

You'll skip some steps - _Closing_

- Import Pakcages and Functions   
**`from sqlalchemy import create_engine`**

- Create the DataBase Engine   
**`import pandas as pd`**

- Connect to the Engine   
**`engine = create_engine('sqlite:///Database_Name.sqlite')`**  

- Context Manager into role
**`with engine.connect() as con:`**   
              **`rs = con.execute("SELECT * from Table_Name")`**   
              **`df = pd.DataFrame(rs.fetchall())`** 
              **`df.colums = rs.keys()`**
