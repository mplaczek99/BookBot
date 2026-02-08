def get_book_texts(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def word_counter(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")
    return num_words

def main():
    text = get_book_texts("books/frankenstein.txt")
    word_counter(text)

main()
