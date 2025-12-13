import random

def create_key():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabet)
    return ''.join(alphabet)

def convert_key(enc_key):
    # Create a map from each letter in the encryption key back to the normal alphabet
    normal_alphabet = "abcdefghijklmnopqrstuvwxyz"
    dec_key = [''] * 26
    for i, char in enumerate(enc_key):
        index = normal_alphabet.index(char)
        dec_key[index] = normal_alphabet[i]
    return ''.join(dec_key)

def translate(text, key):
    normal_alphabet = "abcdefghijklmnopqrstuvwxyz"
    translation_map = {normal_alphabet[i]: key[i] for i in range(26)}
    return ''.join(translation_map.get(c, c) for c in text)

def test_all():
    print("\nStep 1: Creating encryption key...")
    enc_key = create_key()
    print(f"Encryption key: {enc_key}")

    print(f"\nStep 2: Encrypting text...")
    original = "hello this is a secret message"
    encrypted = translate(original, enc_key)
    print(f"Original text: {original}")
    print(f"Encrypted text: {encrypted}")

    print(f"\nStep 3: Converting to decryption key...")
    dec_key = convert_key(enc_key)
    print(f"Decryption key: {dec_key}")

    print(f"\nStep 4: Decrypting text...")
    decrypted = translate(encrypted, dec_key)
    print(f"Decrypted text: {decrypted}")

    print("\nRESULTS:")
    print(f"Original: {original}")
    print(f"Decrypted: {decrypted}")
    print(f"Success? {original == decrypted}")

test_all()
