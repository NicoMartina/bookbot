def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    char_counts = char_counter(text)
    chars_list = convert_dict_to_list(char_counts)
    chars_list.sort(reverse=True, key=sort_on)  # Sort in descending order
    
    for char_dict in chars_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    print("---End Report---")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_counter(text):
    dictionary = {}
    for c in text.lower():
        if c.isalpha():
            if c in dictionary:
                dictionary[c] = dictionary[c] + 1
            
            else:
                dictionary[c] = 1

    return dictionary

def convert_dict_to_list(dictionary):
    char_list = []
    for char, count in dictionary.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)
    return char_list

def sort_on(dictionary):
    return dictionary["count"]
main()

