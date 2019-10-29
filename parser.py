
from random import choice
from string import ascii_letters

def random_characters_returner(number):
    "Returns a string of character with lenght in number form provided."
    string = []
    for number in range(number):
        string.append(choice(ascii_letters))

    print("".join(string))

def string_enconder_64(string):
    "Returns a string encoded in base64."
    pass
def decoder_64(encoded_string):
    "Returns an encoded base64 string decoded."
    pass

random_characters_returner(25)