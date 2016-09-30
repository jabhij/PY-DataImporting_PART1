"""
Instructions --

- Import the functions urlopen and Request from the subpackage urllib.request.
- Package the request to the url "http://www.datacamp.com/teach/documentation" using the function Request() and assign it to request.
- Send the request and catch the response in the variable response with the function urlopen().
- Run the rest of the code to see the datatype of response and to close the connection!
"""

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()
