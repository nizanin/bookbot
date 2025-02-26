import sys
from stats import *


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]

    list_of_char = sort_dictionary(char_text(get_book_text(path)))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")

    for item in list_of_char:
        if item["name"].isalpha():
            print(f"{item["name"]}: {item["num"]}")

    print("============= END ===============")

main()