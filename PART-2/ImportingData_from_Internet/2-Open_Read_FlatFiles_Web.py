"""
Instructions --

•	Assign the URL of the file to the variable url.
•	Read file into a DataFrame df using pd.read_csv(), recalling that the separator in the file is ';'.
•	Print the head of the DataFrame df.
•	Execute the rest of the code to plot histogram of the first feature in the DataFrame df.
"""

# Import packages
import matplotlib.pyplot as plt
import pandas as pd

# Assign url of file: url
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

# Read file into a DataFrame: df
df = pd.read_csv(url, sep=';')

# Print the head of the DataFrame
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()
