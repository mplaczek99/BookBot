def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_characters(text):
    characters = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def sort_characters(characters):
    sorted_list = []

    for char, count in characters.items():
        if char.isalpha(): # Ignore spaces/punctuation
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=find_num)
    return sorted_list

def find_num(characters):
    return characters["num"]
