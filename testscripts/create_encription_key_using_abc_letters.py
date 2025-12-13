def create_new_key(): # Function to create an encryption key using abc letters
    import random
    import string
    letters = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    key = ''.join(random.choice(letters) for i in range(16))  # 16-letter key
    return key

def convert_key(enc_key): # return dec_key
    dec_key = enc_key[::-1]  # Simple conversion: reverse the key
    return dec_key

def enc_dec_text(test, key):
    transformed_text = []
    key_length = len(key)
    for i, char in enumerate(test):
        key_char = key[i % key_length]
        # Simple transformation: shift char by position of key_char in alphabet
        shift = ord(key_char) - ord('a')
        new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a')) if char.islower() else chr(((ord(char) - ord('A') + shift) % 26) + ord('A')) if char.isupper() else char
        transformed_text.append(new_char)
    return ''.join(transformed_text)

def test_all():
    text = 'hello world'
    enc_key = create_new_key()
    dec_key = convert_key(enc_key)
    etext = enc_dec_text(text, enc_key)
    dtext = enc_dec_text(etext, dec_key)
    print(f"Original Text: {text}")
    print(f"Encrypted Text: {etext}")
    print(f"Decrypted Text: {dtext}")

test_all()