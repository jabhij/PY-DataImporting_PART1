"""
Instructions --

- Complete the arguments of np.loadtxt(): the file you're importing is tab-delimited, you want to skip the first row and you only want to 
import the first and third columns.
- Complete the argument of the print() call in order to print the entire array that you just imported.
"""

# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])

# Print data
print(data)
