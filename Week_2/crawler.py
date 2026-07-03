# import requests
# import pandas as pd

# API URL
# url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)
# print(response.json())

# posts = response.json()

# df = pd.DataFrame(posts)
# print(df)

# df.to_csv("posts.csv", index = False)

import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for page in range(1, 11):
    # HTML Website
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_ = "text")
    authors = soup.find_all("small", class_ = "author")

    for quote, author in zip(quotes, authors):
        if quote is not None:
            quote_text = quote.text
        else:
            quote_text = "Not Found"

        if author is not None:
            author_text = author.text
        else:
            author_text = "Not Found"

        data.append(
        {
        "Quote": quote_text,
        "Author": author_text
        }
)
        print("Quote:", quote_text)
        print("Author:", author_text)
        print()
    
df = pd.DataFrame(data)
df.drop_duplicates(inplace = True)
df.to_csv("Quotes.csv", index = False)