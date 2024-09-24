def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(num_chars)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    # use with to open a file
    with open(path) as f:
        return f.read()
    
def get_num_chars(text):
    chars = list(text.lower())
    num_chars = dict.fromkeys(chars, 0)
    for char in chars:
        num_chars[char] += 1
    return num_chars


main()