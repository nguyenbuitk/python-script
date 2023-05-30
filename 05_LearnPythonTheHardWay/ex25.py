def break_words(stuff):
    words = stuff.split(' ')
    return words


def sort_words(words):
    return sorted(words)
    

def print_first_word(words):
    word = words.pop(0)
    print(word)
