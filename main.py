def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(num_chars)

def get_num_words(text):
    # create list of strings from original string split on white space
    words = text.split()
    return len(words)

def get_book_text(path):
    # use with to open a file and "as" to put into variable
    with open(path) as f:
        return f.read()
    
def get_num_chars(text):
    num_chars = {}
    for c in text:
        # lower each character with the lower method
        lowered = c.lower()
        if lowered in num_chars:
            num_chars[lowered] += 1
        else:
            # if character is not initialized as key initialize it as 1 instance
            num_chars[lowered] = 1
    return num_chars

main()