"""
Instructions --

- Complete the first call to np.loadtxt() by passing file as the first argument.
- Execute print(data[0]) to print the first element of data.
- Complete the second call to np.loadtxt(). The file you're importing is tab-delimited, the datatype is float, and you want to skip the 
first row.
- Print the 10th element of data_float by completing the print command. Be guided by the previous print() call.
- Execute the rest of the code to visualize the data.
"""

# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
