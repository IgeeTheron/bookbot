def get_num_words(file_contents):
    return len(file_contents.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    list_of_chars = []

    for ch in num_chars_dict:
        list_of_chars.append({"char": ch, "num": num_chars_dict[ch]})

    list_of_chars.sort(reverse=True, key=sort_on)

    return list_of_chars