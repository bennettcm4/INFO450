import requests

print("Please enter your name: ")
name = input()
url = f"http://localhost:5000/hello/{name}"
response = requests.get(url)
print(response.text)

