def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    if len(letter_guessed) ==1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        old_letters_guessed.sort()
        print(' -> '.join(old_letters_guessed))
        return False
