"""
Instructions --

- Complete the sep (the pandas version of delim), comment and na_values arguments of pd.read_csv(). comment takes characters that comments
occur after in the file, which in this case is '#'. na_values takes a list of strings to recognize as NA/NaN.
- Execute the rest of the code to print the head of the resulting DataFrame and plot the histogram of the 'Age' of passengers aboard the 
Titanic.
"""

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
