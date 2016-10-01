"""
Instructions --

- Pass the variable url to the requests.get() function in order to send the relevant request and catch the response, assigning the 
resultant response message to the variable r.
- Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
- Hit Submit Answer to print the key-value pairs of the dictionary json_data to the shell.
"""

# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
