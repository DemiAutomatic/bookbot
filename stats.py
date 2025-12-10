def get_num_words(text):
    words = text.split()
    return len(words)

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


def get_sorted_chars(char_dict):
    char_dict_array = []

    for char, count in char_dict.items():
        char_dict_array.append({"char": char, "num": count})

    
    char_dict_array.sort(reverse=True, key=sort_on)

    return char_dict_array

