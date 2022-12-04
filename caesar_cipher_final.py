alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift_number, option):
    encrypt_decrypt_txt = ""
    for letter in message:
        # This if statement makes sure only the letters from the alphabets are encrypted or decrypted not spaces and symbols
        if letter in alphabets:
            position = alphabets.index(letter)
            if option == "encode":
                new_position = position + shift_number
            elif option == "decode":
                new_position = position - shift_number
            new_letter = alphabets[new_position]
            encrypt_decrypt_txt += new_letter
        else:
            encrypt_decrypt_txt += letter
    print(f"The {option}d message is {encrypt_decrypt_txt}")

# Importing and printing the logo from art.py 
from art import logo
print(logo)

# End process condition
should_end = False

# While loop to make restart possible
while not should_end:
# User inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

# To make higher shift possible
    shift = shift % 26

# Calling the encryption/decryption function
    caesar(message=text, shift_number=shift, option=direction)

# Restart option
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
    print("Goodbye")
