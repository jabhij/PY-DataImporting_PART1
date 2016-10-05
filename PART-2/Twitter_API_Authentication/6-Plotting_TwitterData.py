"""
Instructions --

- Import both matplotlib.pyplot and seaborn, using the aliases plt and sns, respectively.
- Complete the arguments of sns.barplot: the first argument should be the labels to appear on the x-axis; the second argument should be 
the list of the variables you wish to plot, as produced in the previous exercise.
"""

# Import packages
import seaborn as sns
import matplotlib.pyplot as plt


# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
