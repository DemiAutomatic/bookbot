import sys

from stats import (
    get_num_words,
    get_chars_dict,
    get_sorted_chars
)

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_char_array = get_sorted_chars(chars_dict)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for d in sorted_char_array:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
