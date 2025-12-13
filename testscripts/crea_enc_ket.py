def create_encryption_key():
    import random
    import string
    alphabet = list(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'
    random.shuffle(alphabet)
    enc_key = ''.join(alphabet[:16])  # 16-letter key
    return enc_key
# key = create_encryption_key()
# print(f"Encryption Key: {key}")
def convert_key(enc_key):
    dec_key = enc_key[::-1]  # Simple conversion: reverse the key
    return dec_key
