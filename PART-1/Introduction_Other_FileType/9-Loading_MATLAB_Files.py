"""
Instructions --
- Import the package scipy.io.
- Load the file 'albeck_gene_expression.mat' into the variable mat; do so using the function scipy.io.loadmat().
- Use the function type() to print the datatype of mat to the IPython shell.
"""

# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))
