from text_cleaner import clean_text

user_text = input("Enter text: ")

clean_words = clean_text(user_text)

print(clean_words)