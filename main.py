from stats import get_num_words
from stats import get_chars_dict
from stats import chars_dict_to_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(file_contents)
    chars_dict = get_chars_dict(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if (item["char"].isalpha()):
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()