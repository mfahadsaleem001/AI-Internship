import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
print(response.json())

posts = response.json()

df = pd.DataFrame(posts)
print(df)

df.to_csv("posts.csv", index = False)