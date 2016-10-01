"""
Instructions --

- Import the requests package (you're probably pretty good at this by now!).
- Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
- json_data['items'] is a list of items returned from your query: assign the first such item to the variable nyc_loc.
- Hit Submit Answer to print the key-value pairs of the dictionary nyc_loc to the shell.
"""

# Import package
import requests

# Assign URL to variable: url
url = 'http://chroniclingamerica.loc.gov/search/titles/results/?terms=new%20york&format=json'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Select the first element in the list json_data['items']: nyc_loc
nyc_loc = json_data['items'][0]

# Print each key-value pair in nyc_loc
for k in nyc_loc.keys():
    print(k + ': ', nyc_loc[k])
