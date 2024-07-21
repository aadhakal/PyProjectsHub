# The Vigenère Cipher improves on the Caesar Cipher by using a different shift for each letter. 
# Instead of always shifting letters by the same number, the Vigenère Cipher uses a key—a word 
# or phrase—to decide the shift for each letter. This makes it much harder to decrypt because 
# the pattern changes throughout the message.


text = input("Enter the text you want to encrypt:")
custom_key = input("Enter the key you want to use for encryption:")

def vigenere(message, key , direction = 1):
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ''

    for char in message.lower():
        # Append any non-letter character to the final message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            #Define the offset and encrypted/decrypted character
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message
    
def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'Original Text: {text}')
print(f'Key: {custom_key}')

encryption = encrypt(text, custom_key)
print('Encrypted Text:', encryption)

decryption = decrypt(encryption, custom_key)
print(f'Decrypted text: {decryption}')
