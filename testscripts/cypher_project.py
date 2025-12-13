import random
def create_key(): # Function to create an encryption key using abc letters.
    alphabet = "abcdefghijklmnopqrstuvwxyz" # Step 1: Create normal alphabet .
    alphabet_list = list(alphabet) # Step 2: Convert to list.
    random.shuffle(alphabet_list) # Step 3: Shuffle the list randomly.
    enc_key = "".join(alphabet_list) # Step 4: Join the SHUFFLED list back to string.
    return enc_key
# print("Enc Testing:") # test_enc_key = create_key() # print(f"Encryption Key 1: {test_enc_key}") # key2 = create_key() # print(f"Encryption Key 2: {key2}")

def convert_key(enc_key): # Function to convert enc_key to dec_key.
    normal_alphabet = "abcdefghijklmnopqrstuvwxyz" # Step 1: Normal alphabet.
    dec_key = [''] * 26 # Step 2: Create an empty list of 26 chars.
    for l in range(26): # Step 3: For each position in normal alphabet.
        # Find where normal[l] went in enc_key.
        normal_letter = normal_alphabet[l]
        encrypted_letter = enc_key[l]

        # To decrypt, we need the reverse. If 'a' (position 0) became 'x', then 'x' should decrypt back to 'a'.

        position_of_encrypted = ord(encrypted_letter) - ord('a')
        dec_key[position_of_encrypted] = normal_letter
    dec_key = "".join(dec_key)
    return dec_key
# print("Dec Testing:") # test_dec_key = convert_key(test_enc_key) # print(F"Decryption Key: {test_dec_key}") # print()  

def encryption(text, key): # Encryption of text using encryption key
    normal_alphabet = "abcdefghijklmnopqrstuvwxyz" # Step 1: Define norma alphabet.
    result = "" # Step 2: Create an empty result so it will be filled after encryption
    for char in text: # Step 3: A loop to go through each character in text.
        if char in normal_alphabet: # Step 4: Check if it's in there and lower case.
            position = normal_alphabet.index(char) # Find position in normal alphabet.
            encrypted_char = key[position] # Get encrypted letter from key ar same position
            result += encrypted_char
        else: # Step 5: Not a letter (space, punctuation, etc.)
            result += char
    return result # Step 6: Return encrypted text.
# print("Enc text Testing:") # test_key = create_key() # original_text = "hello world" # encrypted_text = encryption(original_text, test_key) # print(f"Original: {original_text}") # print(f"Key: {test_key}") # print(f"Encrypted: {encrypted_text}") # print()

def decryption(text, key): # Using the same logic as the encription function only this time it will use the encrypted text and a decryption key.
    normal_alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in text:
        if char in normal_alphabet:
            position = normal_alphabet.index(char)
            decrypted_char = key[position]
            result += decrypted_char
        else:
            result += char
    return result

def test_all():# Test the complete encryptio/decryption system
    print("\nStep 1: Creating encryption key...")
    enc_key = create_key()
    print(f"Encryption key: {enc_key}")

    print(f"\nStep 2: Encrypting text...")
    original = "hello this is a secrete message"
    encrypted = encryption(original, enc_key)
    print(f"Original text: {original}")
    print(f"Encrypted text: {encrypted}")

    print(f"\nStep 3: Converting to decryption key...")
    dec_key = convert_key(enc_key)
    print(f"Decryption key: {dec_key}")

    print(f"\nStep 4: Decrypting text...")
    decrypted = decryption(encrypted, dec_key)
    print(f"Decrypted text: {decrypted}")
    print()

    print("RESULTS:")
    print(f"Original: {original}")
    print(f"Decrypted: {decrypted}")
    print(f"Success? {original == decrypted}")


test_all()

