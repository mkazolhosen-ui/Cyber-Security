# cipher.py

def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        raise ValueError("Shift must be an integer.")

    shift = shift % 26
    shift = shift if encrypt else -shift

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted + shifted.upper()
    )

    return text.translate(table)


def brute_force(text):
    results = []
    for shift in range(26):
        decrypted = caesar(text, shift, encrypt=False)
        results.append((shift, decrypted))
    return results