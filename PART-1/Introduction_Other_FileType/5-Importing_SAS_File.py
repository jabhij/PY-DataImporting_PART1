"""
Instructions --

- Import the module SAS7BDAT from the library sas7bdat.
- In the context of the file 'sales.sas7bdat', load its contents to a DataFrame df_sas, using the method to_data_frame() on the object 
file.
- Print the head of the DataFrame df_sas.
- Execute your entire script to produce a histogram plot!
"""

# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = SAS7BDAT.to_data_frame(file)

# Print head of DataFrame
print (df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()


"""
PLOT
"""

