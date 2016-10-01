"""
Instructions --

- Import the requests package.
- Assign to the variable url the URL of interest in order to query 'http://www.omdbapi.com' for the data corresponding to the movie The 
Social Netork. The query string should have one argument t=social+network.
- Print the text of the reponse object r by using its text attribute and passing the result to the print() function.
"""

# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?t=social+network' 

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)
