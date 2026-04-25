def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter.lower() not in old_letters_guessed:
            return False
    return True