# Prompt the user to enter a message and store the input in the variable 'text'
text = input("Enter your message: ")

# Initialize an empty string 'cipher' to store the encrypted message
cipher = ''

# Iterate over each character in the user's input text
for char in text:
    # If the character is not an alphabet letter (e.g., digits, punctuation), skip it
    if not char.isalpha():
        continue

    # Convert the character to uppercase
    char = char.upper()

    # Find the ASCII code of the character and add 1 to it to shift it by one position
    code = ord(char) + 1

    # If adding 1 exceeds the ASCII code for 'Z', wrap around to 'A'
    if code > ord('Z'):
        code = ord('A')

    # Convert the shifted ASCII code back to a character and add it to the cipher string
    cipher += chr(code)

# After processing all characters, print the encrypted message
print(cipher)


# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
