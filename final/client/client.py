"""
Must accept user input representing a 'name'
Must make HTTP GET call to server in the form of:
http://localhost:5000/hello/{name}
"""

import requests

print("Please enter your name: ")
name = input()
url = f"http://localhost:5000/hello/{name}"
response = requests.get(url)
print(response.text)