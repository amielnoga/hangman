def is_valid_input(letter_guessed):
    if len(letter_guessed) > 1:
        return False
    if letter_guessed.isalpha()== False:
        return False
    return True



