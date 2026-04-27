HANGMAN_PHOTOS={
    1: "x-------x",
    2: "\n    x-------x\n    |\n    |\n    |\n    |\n    |\n\t",
    3: "\n    x-------x\n    |       |\n    |       0\n    |\n    |\n    |\n\t",
    4: "\n    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |\n\t",
    5: "\n    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |\n    |\n\t",
    6: "\n    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      /\n    |\n\t",
    7: "\n    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      / \\\n    |\n\t"}

def print_hangman(num_of_tries):
    print (HANGMAN_PHOTOS[num_of_tries])