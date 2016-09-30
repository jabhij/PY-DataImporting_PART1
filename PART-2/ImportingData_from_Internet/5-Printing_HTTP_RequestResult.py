"""
Instructions --
- Send the request and catch the response in the variable response with the function urlopen(), as in the previous exercise.
- Extract the response using the read() method and store the result in the variable html.
- Print the string html.
- Hit submit to perform all of the above and to close the response: be tidy!
"""

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://docs.datacamp.com/teach/"

# This packages the request
request = Request(url)

# Sends the request and catches the response: response
response =  urlopen(request)

# Extract the response: html
html = response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()
