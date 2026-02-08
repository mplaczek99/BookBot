from stats import get_num_words

def get_book_texts(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_texts("books/frankenstein.txt")
    get_num_words(text)

main()
