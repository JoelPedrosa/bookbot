def word_count(text):
    word_list = text.split()
    counter = len(word_list)
    return counter

def caracter_count(text):
    word_dict = {}

    for i in text:
        lower_char = i.lower()
        if lower_char in word_dict : 
            word_dict[lower_char] += 1
        else :
            word_dict[lower_char] = 1
    return word_dict

def sort_on(items):
    return items["num"]

def sorted_dict (char_dict) :
    sorted_words = []
    for char, count in char_dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": count}
            sorted_words.append(new_dict)
    sorted_words.sort(reverse=True, key=sort_on)
    return sorted_words
