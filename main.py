def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text("books/frankenstein.txt")
    print(text)
    words = number_of_words(text)
    print(words)

    characters = character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(characters)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    split_words = text.split()
    return len(split_words)

def character_count(text):
    character_dict = {}
    lowercase_string = text.lower()
    for char in lowercase_string:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1    
    return character_dict

def sort_on(dict):
    return dict["num"]
       

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 







main()