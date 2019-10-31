#!/usr/bin/env python

import base64
from random import choice
from string import ascii_letters
import sys

def random_characters(lenght):
    "Returns a string of character with lenght in number form provided."
    string = []
    for number in range(lenght):
        string.append(choice(ascii_letters))

    return "".join(string)

def encode_string_64(string):
    "Returns a string encoded in base64."
    encodedString = base64.b64encode(string.encode("utf-8"))
    return str(encodedString, "utf-8")

def decode_string_64(encoded_string):
    "Returns an encoded base64 string decoded."
    decodedString = base64.b64decode(encoded_string)
    return str(decodedString, "utf-8")

if sys.argv:
    print('ok')