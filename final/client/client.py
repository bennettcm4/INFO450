"""
Must accept user input representing a 'name'
Must make HTTP GET call to server in the form of:
http://localhost:5000/hello/{name}
"""

import requests

r = requests.get("http://localhost:5000/hello{name}")
print(r.text)