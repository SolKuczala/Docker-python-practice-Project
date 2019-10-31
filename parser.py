#!/usr/bin/env python

import base64
import argparse
from random import choice
from string import ascii_letters
import sys

def random_characters(lenght):
    "Returns a string of character with the lenght of the number provided."
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

#mis comandos finales son:
#grsed r {number}
#grsed e {string}
#grsed d {encoded string}
#
actions = {
    'r' : (random_characters,int),
    'e' : (encode_string_64,str),
    'd' : (decode_string_64,str)
}
# print(actions.keys()) # devuelve array de keys

input_option = sys.argv[1]
input_value = sys.argv[2]

result = None
try:
    function, parser = actions[input_option]
    result = function(parser(input_value))
except Exception as e:
    print('invalid action')
    exit(1)
    
print(result)