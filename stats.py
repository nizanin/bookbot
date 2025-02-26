def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def num_words(text):
    return len(text.split())

def char_text(text):
    dict_ = {}
    for char in text:
        dict_[char.lower()] = dict_.get(char.lower(), 0) + 1
    return dict_

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dict):
    list = [{"name": key, "num": value} for (key, value) in dict.items()]
    list.sort(reverse=True, key=sort_on)
    return list