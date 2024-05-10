def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    words = number_of_words(text)
    print(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    split_words = text.split()
    total_words = 0
    for word in split_words:
        total_words += 1
    return total_words

main()