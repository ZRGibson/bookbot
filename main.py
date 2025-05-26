from stats import get_num_words, get_num_chars

def get_book_text(book_path):
    with open(book_path) as file:
        book_read = file.read()
    return book_read 


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_path)
    num_chars = get_num_chars(book_path)
    print(f"{num_words} words found in the document")
    print(num_chars)


main()