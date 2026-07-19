import requests
import webbrowser

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    webbrowser.open("https://jsonplaceholder.typicode.com/users")
users = response.json()
print(users[0]["name"])
data = {
    "title": "Python",
    "body": "Learning Requests",
    "userId": 1
}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.status_code)
print(response.request.body)
