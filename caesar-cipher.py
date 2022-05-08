from hashlib import new
from black import out
from numpy import char

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('''

 __    __     _                            _                     
/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___               
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \              
 \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |             
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/              
                                                                 
   ___                               ___ _       _               
  / __\__ _  ___  ___  __ _ _ __    / __(_)_ __ | |__   ___ _ __ 
 / /  / _` |/ _ \/ __|/ _` | '__|  / /  | | '_ \| '_ \ / _ \ '__|
/ /__| (_| |  __/\__ \ (_| | |    / /___| | |_) | | | |  __/ |   
\____/\__,_|\___||___/\__,_|_|    \____/|_| .__/|_| |_|\___|_|   
                                          |_|                    
''')

# def encrypt(text, shift):
#     encrypted_string = ""
#     for character in text:
#         index = alphabet.index(character)
#         new_position = index + shift
#         if new_position > 25:
#             new_position -= 26
#         encrypted_string += alphabet[new_position]
#     print(f"Your encrypted message is {encrypted_string}")


# def decrypt(text, shift):
#     decrypted_string = ""
#     for character in text:
#         index = alphabet.index(character)
#         decrypted_string += alphabet[index - shift]
#     print(f"Your decrypted message is {decrypted_string}")

# if operation == "1":
#     encrypt(text, shift)
# elif operation == "2":
#     decrypt(text, shift)

def caesar(text, shift, operation):
    output_string = "" # An empty string for storing the resultant text.
    type_of_operation = ["encode", "decode"]
    for character in text:
        if ord(character) >= 97 and ord(character) <= 122: # Checking for the lower case characters only.
            index = alphabet.index(character)
            if operation == "1":
                output_string += alphabet[(index + shift) % 26]
            elif operation == "2":
                output_string += alphabet[(index - shift) % 26]
        else:
            output_string += character

    print(f"Your {type_of_operation[int(operation) - 1]} message is {output_string}")

terminate_program = False

while terminate_program != True:
    
    operation = input("Select an option:\n1. Encrypt\n2. Decrypt\n") # Prompt the user to choose the operation.

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, operation) # Calling of the Caesar function.

    user_input = input("Do you want to continue? (Y/N) ").lower()
    if user_input == "n":
        terminate_program = True
        print("Goodbye")
