from stats import get_num_words, get_num_chars, get_ordered_list

def main():
    book_path = "books/frankenstein.txt"
    num_words = get_num_words(book_path)
    num_chars = get_num_chars(book_path)
    ordered_list = get_ordered_list(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in ordered_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()