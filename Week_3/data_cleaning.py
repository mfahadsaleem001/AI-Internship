# Imports
import re
import pandas as pd

# Read CSV
df = pd.read_csv("Quotes.csv")

# print(df.head(3))
# print(df.tail(3))
# print(df.shape)
# print(df.columns)
# df.info()

#Function For Remove Links
def remove_links(text):
    clean_text = re.sub(r"https?://\S+", "", text)
    return clean_text
df["Quote"] = df["Quote"].apply(remove_links)

#Function For Remove HTML
def remove_html(text):
    clean_text = re.sub(r"<.*?>","", text)
    return clean_text
df["Quote"] = df["Quote"].apply(remove_html)

#Function For Remove Posts
def remove_short_posts(text):
    if len(text) < 10:
        return None
    else:
        return text
df["Quote"] = df["Quote"].apply(remove_short_posts)
    
df.dropna(inplace = True)
df.to_csv("clean_quotes.csv", index=False)