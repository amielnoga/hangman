
def check_win(secret_word, old_letters_guessed):
    """ The function checks if all the letters that make up the secret word are included in the list of letters that the user guessed.
     :param secret_word: the word to check.
     :param old_letters_guessed: the guessed letters.
     :type secret_word: String
     :type old_letters_guessed: list
     :return: True if all the letters of the word is in the guessed letters, False otherwise.
     :rtype: bool
     """
    for letter in secret_word:
        if letter.lower() not in old_letters_guessed:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    """The function returns a string consisting of letters and underscores.
     The string displays the letters from the list old_letters_guessed that are in the string secret_word in their
     appropriate positions, and the remaining letters in the string (those the player has not yet guessed) as underscores.
     :param secret_word: String the word to check.
     :param old_letters_guessed: the guessed letters.
     :type secret_word: String
     :type old_letters_guessed: list
     :return: letters and underscores
     :rtype: String """
    string =""
    for letter in secret_word:
        if letter in old_letters_guessed:
            string += letter
        else:
            string += '_'
        string += ' '
    return string[:-1]

def check_valid_input(letter_guessed, old_letters_guessed):
    """ The function accepts a character and a list of letters that the user has guessed before. The function checks two
     things: the validity of the input and whether it is legal to guess this letter (i.e., the player has not guessed
     this letter before) and returns true or false accordingly.
     :param letter_guessed: guessed letter.
     :param old_letters_guessed: the old guessed letters.
     :type letter_guessed: String
     :type old_letters_guessed: list
     :return: True if the input is valid, False otherwise.
     :rtype: bool"""
    if len(letter_guessed) > 1:
        return False
    if not letter_guessed.isalpha():
        return False
    if letter_guessed.lower() in old_letters_guessed:
        return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ The function uses the check_valid_input function to determine whether the character is valid and has not been
    guessed before, or if the character is invalid and/or is already in the guess list.
    If the character is invalid or has been guessed before, the function prints the character X
    (as an uppercase letter), below it the list of letters that have already been guessed, and returns false. If the
    character is valid and has not been guessed before, the function adds the character to the guess list and
    returns true.
    :param letter_guessed: the guessed letters.
    :param old_letters_guessed: the old guessed letters.
    :type letter_guessed: String
    :type old_letters_guessed: list
    :return: True if the character is valid and has not been guessed before, False otherwise.
    :rtype: bool"""
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        if len(old_letters_guessed) > 0:
            old_letters_guessed.sort()
            print(' -> '.join(old_letters_guessed))
        return False

def choose_word(file_path, index):
    """ The function accepts as parameters: a string representing a path to a text file containing words separated by
     spaces, and an integer representing the position of a particular word in the file.
    The function returns the word at the position received as an argument to the function (index), which will be used as
     the secret word for guessing.
     :param file_path: the path to a text file containing words separated by spaces.
     :param index: Integer representing the position of the word in the file (counting from 1).
     :type file_path: String
     :type index: Integer
     :return: String containing the word at the position received as an argument.
     :rtype: String"""
    with open(file_path) as file:
        words = file.read().split(' ')
        words_number=len(words)
    return words[(index-1) % words_number]

def print_welcome_message(MAX_TRIES):
    """The function prints a welcome message to the user.
    :param MAX_TRIES: the maximum number of wrong guesses allowed.
    :type MAX_TRIES: Integer
    :return: None
    """
    print("Welcome to the game Hangman")
    print(r""" 
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/
    """)
    print(MAX_TRIES)

def print_hangman(HANGMAN_PHOTOS,num_of_tries):
    """The function prints the hangman to the user according to the number of tries.
    :param HANGMAN_PHOTOS: The photos of the hangman.
    :type HANGMAN_PHOTOS: Dictionary
    :param num_of_tries: the number of tries.
    :type num_of_tries: Integer
    :return: None"""
    print (HANGMAN_PHOTOS[num_of_tries])

def main():
    MAX_TRIES = 6
    HANGMAN_PHOTOS = {
        1: "    x-------x",
        2: "    x-------x\n    |\n    |\n    |\n    |\n    |\n\t",
        3: "    x-------x\n    |       |\n    |       0\n    |\n    |\n    |\n\t",
        4: "    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |\n\t",
        5: "    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |\n    |\n\t",
        6: "    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      /\n    |\n\t",
        7: "    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      / \\\n    |\n\t"}
    current_num_of_tries = 0
    old_letters_guessed = []
    print_welcome_message(MAX_TRIES)
    path = input(r"Enter file path: ")
    index = int(input("Enter index: "))
    secret_word = choose_word(path, index)
    print("\nLet’s start!\n")
    print_hangman(HANGMAN_PHOTOS, 1)
    print(show_hidden_word(secret_word, old_letters_guessed))
    while current_num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        guess_status = False
        while not guess_status:
            guessed_letter = input("Guess a letter: ")
            guess_status = try_update_letter_guessed(guessed_letter, old_letters_guessed)
        # guess_status == True
        if guessed_letter.lower() not in secret_word.lower():
            current_num_of_tries+=1
            print(":(")
            print_hangman(HANGMAN_PHOTOS, current_num_of_tries + 1)
        print(show_hidden_word(secret_word, old_letters_guessed))

    if check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print("LOSE")

if __name__ == '__main__':
    main()