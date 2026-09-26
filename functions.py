import string

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