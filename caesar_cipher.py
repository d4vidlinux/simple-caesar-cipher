#!/usr/bin/env python3

# Simple Caesar cipher  

import argparse
from functions import encrypt, decrypt

print("="*6, "Caesar cipher", "="*6)

def main():
    parser = argparse.ArgumentParser(description="Caesar cipher")
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-e", "--encrypt", help="Encrypt the text", action="store_true")
    group.add_argument("-d", "--decrypt", help="Decrypt the encrypted text", action="store_true")
    parser.add_argument("-s", "--shift", help="Enter the shift for encrypt/decrypt", type=int, required=True)
    parser.add_argument("text", help="Enter the text for encrypt/decrypt")

    args = parser.parse_args()

    text = args.text
    shift = args.shift

    if shift < 1 or shift > 25:
        print("\n\033[31mERROR: Shift must be between 1 and 25\033[0m\n")
        exit(1)

    if args.encrypt:
        print("\n", encrypt(text, shift), "\n")

    elif args.decrypt:
        print("\n", decrypt(text, shift), "\n")

if __name__ == "__main__":
    main()



