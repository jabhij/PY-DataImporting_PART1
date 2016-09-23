"""
Instructions --

- Open moby_dick.txt using the with context manager and the variable file.
- Print the first three lines of the file to the shell by using readline() three times within the context manager.
"""

# Read & print the first 3 lines
with open('moby_dick.txt') as file:
    
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
