def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_chars = []

    # create new dictionary for each key pair in num_chars and add to sorted_chars
    for char in num_chars:
        sorted_chars.append({char: num_chars[char]})

    sorted_chars.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for c in sorted_chars:
        key = list(c.keys())[0]
        value = list(c.values())[0]
        print(f"The {key} character was found {value} times")
    print("--- End report ---")

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
        # check if key is alphabetic character
        if c.isalpha() == True:
            if lowered in num_chars:
                num_chars[lowered] += 1
            else:
                # if character is not initialized as key initialize it as 1 instance
                num_chars[lowered] = 1
    return num_chars

def sort_on(dict):
    return list(dict.values())[0]

main()