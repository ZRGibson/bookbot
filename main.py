def get_book_text(book_path):
    with open(book_path) as file:
        book_read = file.read()
    return book_read 


def get_num_words(book_path):
    word_count = 0
    with open(book_path) as file:
        book_read = file.read()
        for word in book_read.split():
            word_count += 1  
        return word_count  


#def main():
    #book_path = "books/frankenstein.txt"
    #book_text = get_book_text(book_path)
    #print(book_text)


def main():
    book_path = "books/frankenstein.txt"
    num_words = get_num_words(book_path)
    print(f"{num_words} words found in the document")


main()