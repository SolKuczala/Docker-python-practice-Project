import base64
from random import choice
from string import ascii_letters

def random_characters_returner(number):
    "Returns a string of character with lenght in number form provided."
    string = []
    for number in range(number):
        string.append(choice(ascii_letters))

    return "".join(string)

def string_encoder_64(string):
    "Returns a string encoded in base64."
    encodedBytes = base64.b64encode(string.encode("utf-8"))
    return str(encodedBytes, "utf-8")

def decoder_64(encoded_string):
    "Returns an encoded base64 string decoded."
    decodedBytes = base64.b64decode(encoded_string)
    return str(decodedBytes, "utf-8")


print()