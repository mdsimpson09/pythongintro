def print_upper_words(words):
    """ print our each word on a seaprate line, all uppercase 
    """
    for word in words:
        print (word.upper())

def print_words_again(words):
    """ change function so that it only prints words that start with 'e'
        can be uppercase or lowercase 
    """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word)

        