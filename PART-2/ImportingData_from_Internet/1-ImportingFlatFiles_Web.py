"""
Instructions—

•	Import the function urlretrieve from the subpackageurllib.request.
•	Assign the URL of the file to the variable url.
•	Use the function urlretrieve() to save the file locally as'winequality-red.csv'.
•	Execute the remaining code to load 'winequality-red.csv'in a pandas DataFrame and to print its head to the shell.
"""

# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())
