from string import ascii_lowercase


def valid_word(word):
    for char in word:
        if char not in ascii_lowercase:
            return False

    return True
