from stats import countWords
from stats import countCharacters
from stats import sortedDict
import sys


def get_book_text():
    with open(sys.argv[1]) as book:
        return book.read()


def main():
    #    numWords = countWords(get_book_text())
    #   print(f"Found {numWords} total words")
    #  numChars = countCharacters(get_book_text())
    # print(numChars)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    numWords = countWords(text)
    print(f"Found {numWords} total words")
    print("--------- Character Count -------")
    counts = countCharacters(text)
    items = sortedDict(counts)
    for item in items:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
