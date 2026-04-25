def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1:
        return False
    if letter_guessed.isalpha()== False:
        return False
    if letter_guessed.lower() in old_letters_guessed:
        return False
    return True



