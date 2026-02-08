def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_characters(text):
    characters = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters
