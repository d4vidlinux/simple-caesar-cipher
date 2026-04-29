#!/usr/bin/env python3

# Simple Caesar Cipher  

import string

print("="*6, "Caesar Cipher", "="*6)


def caesar(text, shift, encrypt=True):
    
    alphabet = string.ascii_letters

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

phrase = input("Write the phrase: ")

try:

    shift = int(input("The shift: "))
        
    if shift < 1 or shift > 25:
        print("ERROR: Shift must be an integer between 1 and 25")
        exit()

except ValueError:
    print("ERROR: Shift must be an integer")
    exit()

ask2 = input("Encrypt or Decrypt this phrase? [e/d] ")

if ask2.lower() == "e":
    print(encrypt(phrase, shift))

elif ask2.lower() == "d":
    print(decrypt(phrase, shift))