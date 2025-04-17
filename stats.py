def get_num_words(text):
    return len(text.split())

def get_character_counts(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if not char in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def sort_chars(char_count_dict):
    sorted = []
    for char in char_count_dict:
        count = char_count_dict[char]
        sorted.append({"char": char, "count": count})
    sorted.sort(reverse=True, key=sort_on)
    return sorted