from stats import get_num_words, get_character_counts, sort_chars
import sys

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = args[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = sort_chars(get_character_counts(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_counts:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()