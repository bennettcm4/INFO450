"""
Must accept a path /hello with a parameter for 'name'
Return value must be a dictionary with the key 'hello' and the value of the name url parameter
Server should listen on port 5000
"""

from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return {"Hello": name}

