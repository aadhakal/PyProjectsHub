# The Caesar Cipher is a classic encryption technique used in ancient times,
# named after Julius Caesar. It works by shifting the letters of the alphabet 
# by a fixed number of positions. For example, with a shift of 3, 'A' becomes 'D', 'B' 
# becomes 'E', and so on. This simple yet effective method provides basic text encryption 
# and decryption.


text = input("Enter the text you want to encrypt:")
shift  = 3 # you can change the shift value to any number you want


def caesar(message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ''

    for char in message.lower():  
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift)% len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain Text:', message)
    print(f"The encrypted text is: {encrypted_text}")

caesar(text, shift)


