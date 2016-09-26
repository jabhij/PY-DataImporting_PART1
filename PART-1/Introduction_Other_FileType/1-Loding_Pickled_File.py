"""
Instructions --

- Import the pickle package.
- Complete the second argument of open() so that it is read only for a binary file. This argument will be a string of two letters, one 
signifying 'read only', the other 'binary'.
- Pass the correct argument to pickle.load(): it should use the variable that is bound to open.
- Print the data d.
- Print the datatype of d; take your mind back to your previous use of the function type().
"""

# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))
