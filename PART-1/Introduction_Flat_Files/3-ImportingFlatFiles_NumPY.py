"""
Instructions --

- Fill in the arguments of np.loadtxt() by passing file and a comma ',' for the delimiter.
- Fill in the argument of print() to print the type of the object digits. Use the function type().
- Execute the rest of the code to visualize one of the rows of the data.
"""

# Import package
import numpy as np

# Assign filename to variable: file
file = 'digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()
