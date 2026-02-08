from stats import get_num_words, get_characters, sort_characters

def get_book_texts(filepath):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    text = get_book_texts("books/frankenstein.txt")

    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    characters = get_characters(text)
    sorted_characters = sort_characters(characters)
    for character in sorted_characters:
        print(f"{character['char']}: {character['num']}")

    print("============= END ===============")

main()
