from stats import get_num_words, get_num_characters

def get_book_texts(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_texts("books/frankenstein.txt")

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    characters = get_num_characters(text)
    print(characters)

main()
