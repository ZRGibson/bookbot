def get_num_words(book_path):
    word_count = 0
    with open(book_path) as file:
        book_read = file.read()
        for word in book_read.split():
            word_count += 1  
        return word_count 
    
def get_num_chars(book_path):
    char_count = {}
    with open(book_path) as file:
        book_read = file.read()
        for char in book_read.lower():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1   
        return char_count
    