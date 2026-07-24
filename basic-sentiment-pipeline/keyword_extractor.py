from text_cleaner import clean_text

def extract_keywords(text):

    clean_words = clean_text(text)

    frequency = {}

    for word in clean_words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

    sorted_keywords = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_keywords