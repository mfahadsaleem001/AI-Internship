import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print(response.json())

posts = response.json()
print(posts)

for post in response.json():
    print(post["title"])