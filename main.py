def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(num_chars)

def get_num_words(text):
    # create list of strings from orginal string split on white space
    words = text.split()
    return len(words)

def get_book_text(path):
    # use with to open a file and "as" to put into variable
    with open(path) as f:
        return f.read()
    
def get_num_chars(text):
    # make text into lower case list and create dictionary from it with initialized value of 0
    chars = list(text.lower())
    num_chars = dict.fromkeys(chars, 0)
    # add up running tallies for each character
    for char in chars:
        num_chars[char] += 1
    return num_chars


main()