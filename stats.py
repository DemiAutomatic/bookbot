def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    counts = {}
    for word in text.split():
        for char in word:
            char = char.lower()
            if not char in counts:
                counts[char] = 1
            else:
                counts[char] += 1
    return counts

def sort_on(dict):
    return dict["count"]

def sort_chars(chars):
    sorted = []
    for char in chars:
        count = chars[char]
        sorted.append({"char": char, "count": count})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
