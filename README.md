# Caesar Cipher

A simple command-line Caesar cipher implemented in Python.

This project was created as a small exercise in Python, focusing on command-line arguments, modular code organization, and basic text encryption/decryption.

## Features

* Encrypt text using a Caesar cipher
* Decrypt encrypted text
* Command-line interface using `argparse`
* Encrypt/decrypt modes are mutually exclusive
* Configurable shift value
* Separate cipher logic from the CLI
* Input validation for the shift value

## Project Structure

```text
caesar-cipher/
├── caesar_cipher.py
└── functions.py
```

### `caesar_cipher.py`

Responsible for the command-line interface and argument handling.

It uses `argparse` to handle:

* `-e` / `--encrypt`
* `-d` / `--decrypt`
* `-s` / `--shift`
* `text`

### `functions.py`

Contains the Caesar cipher logic:

* `caesar()`
* `encrypt()`
* `decrypt()`

## Requirements

* Python 3

No external Python packages are required.

## Usage

### Encrypt

```bash
python3 caesar_cipher.py -e -s 3 "hello world"
```

Example output:

```text
khoor zruog
```

### Decrypt

```bash
python3 caesar_cipher.py -d -s 3 "khoor zruog"
```

Example output:

```text
hello world
```

## Arguments

| Argument          | Description                    |
| ----------------- | ------------------------------ |
| `-e`, `--encrypt` | Encrypt the text               |
| `-d`, `--decrypt` | Decrypt the text               |
| `-s`, `--shift`   | Shift value used by the cipher |
| `text`            | Text to encrypt or decrypt     |

The `-e` and `-d` options are mutually exclusive, and one of them is required.

The shift must be an integer between `1` and `25`.

## How It Works

The Caesar cipher replaces each letter with another letter a fixed number of positions away in the alphabet.

For example, with a shift of `3`:

```text
a → d
b → e
c → f
...
x → a
y → b
z → c
```

The project uses Python's `string` and `str.translate()` functionality to perform the character substitution.

## Examples

Encrypt:

```bash
python3 caesar_cipher.py -e -s 5 "Hello"
```

Decrypt:

```bash
python3 caesar_cipher.py -d -s 5 "Mjqqt"
```

## Learning Goals

This project was also used to practice:

* Functions
* Modules
* Imports
* `argparse`
* Command-line flags
* Mutually exclusive arguments
* Argument validation
* `if __name__ == "__main__"`
* Basic project organization

## Author

**d4vidlinux**
