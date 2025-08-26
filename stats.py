import string

def get_num_words(file_contents):
    return len(file_contents.split())

def get_num_caracters(file_contents):
    alphabet_dict = {letter: 0 for letter in string.ascii_lowercase}
    list_of_chars = list(file_contents)

    for char in list_of_chars:
        char = char.lower()
        if (char in alphabet_dict):
            alphabet_dict[char] += 1
    

    return alphabet_dict