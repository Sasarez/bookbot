def generate_report(character_dict):
    sorted_dict = dict(sorted(character_dict.items()))

    for character in list(sorted_dict.keys()):
        if not character.isalpha():  # If the key is not alphabetical
            del sorted_dict[character]

    for character in sorted_dict:
        print(f"The '{character}' character appears {sorted_dict[character]} times")



def character_count(book_text):
    char_dict = {}
    book = book_text.lower()
    words = book.split(" ")
    for word in words:
        for character in word:
            try:
                current_value = char_dict[character]
            except:
                current_value = 0
            current_value += 1
            char_dict[character] = current_value
    return (char_dict)

def wordcount(book_text):
    amount = 0
    words = book_text.split()
    character_dict = character_count(book_text)
    generate_report(character_dict)
    return (len(words))

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print (file_contents)
    wc = wordcount(file_contents)
    print (f"There are {wc} words in this document")
    
main()

