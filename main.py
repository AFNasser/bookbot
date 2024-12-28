def main():
    bookpath = "./books/frankenstein.txt"
    with open(bookpath) as file:
        file_contents = file.read()
    
    word_count = count_words(file_contents)
    char_counts = count_chars(file_contents)

    create_report(bookpath, word_count, char_counts)

def count_words(long_string):
    words = long_string.split()
    num_of_words = len(words)

    return num_of_words

def count_chars(long_string):
    char_dict = {
                "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0,
                "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0,
                "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
                }

    for c in long_string.lower():
        if c in char_dict:
            char_dict[c] += 1

    sorted_char_dict = sort_by_count(char_dict)

    return sorted_char_dict

def sort_by_count(input_dict):
    item_list = list(input_dict.items())
    item_list.sort(reverse=True, key=sort_on)

    result_dict = dict(item_list)
    
    return result_dict

def sort_on(input_tuple):
    return(input_tuple[1])

def create_report(path, number_of_words, character_dictionary):
    print(f"---- BOOKBOT REPORT > {path} ----\n")
    print(f"Book contains {number_of_words} words.\n")
    print("Character Breakdown:")
    for c in character_dictionary:
       print(f"Letter '{c}' found {character_dictionary[c]} times.")
    print("\n---- END OF REPORT ----")

main()