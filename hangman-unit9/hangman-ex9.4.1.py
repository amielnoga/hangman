from os.path import split

from numpy.ma.extras import unique


def choose_word(file_path, index):
    with open(file_path) as file:
        words = file.read().split(' ')
        unique_words = set(words)
        words_number=len(words)
    return len(unique_words), words[(index-1)%words_number]