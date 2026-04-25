def show_hidden_word(secret_word, old_letters_guessed):
    string =""
    for letter in secret_word:
        if letter in old_letters_guessed:
            string += letter
        else:
            string +='_'
        string += ' '
    return string[:-1]