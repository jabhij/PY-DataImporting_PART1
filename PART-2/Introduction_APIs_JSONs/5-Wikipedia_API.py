"""
Instructions --

- Assign the relevant URL to the variable url.
- Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
- The variable pizza_extract holds the HTML of an extract from Wikipedia's Pizza page as a string; use the function print() to print 
this string to the shell.
"""

# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
