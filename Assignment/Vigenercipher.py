import string

# Function to generate the repeating key
def generate_repeating_key(message, keyword):
    keyword = list(keyword)
    if len(message) == len(keyword):
        return ''.join(keyword)
    else:
        for i in range(len(message) - len(keyword)):
            keyword.append(keyword[i % len(keyword)])
    return ''.join(keyword)

# Function to encode a message using the Vigenère cipher
def encode(message, key):
    encoded_message = []
    for i in range(len(message)):
        if message[i].isupper():
            encoded_message.append(chr((ord(message[i]) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A')))
        elif message[i].islower():
            encoded_message.append(chr((ord(message[i]) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a')))
        elif message[i].isdigit():
            encoded_message.append(chr((ord(message[i]) + ord(key[i]) - 2 * ord('0')) % 10 + ord('0')))
        else:
            encoded_message.append(message[i])  # Keep special characters unchanged
    return ''.join(encoded_message)

# Function to decode an encoded message using the Vigenère cipher
def decode(encoded_message, key):
    decoded_message = []
    for i in range(len(encoded_message)):
        if encoded_message[i].isupper():
            decoded_message.append(chr((ord(encoded_message[i]) - ord(key[i]) + 26) % 26 + ord('A')))
        elif encoded_message[i].islower():
            decoded_message.append(chr((ord(encoded_message[i]) - ord(key[i]) + 26) % 26 + ord('a')))
        elif encoded_message[i].isdigit():
            decoded_message.append(chr((ord(encoded_message[i]) - ord(key[i]) + 10) % 10 + ord('0')))
        else:
            decoded_message.append(encoded_message[i])  # Keep special characters unchanged
    return ''.join(decoded_message)

# Original message and key
message = input("Enter the message: ")
keyword = input("Enter the keyword: ")

# Generate repeating key
key = generate_repeating_key(message, keyword)

# Encode the message
encoded_message = encode(message, key)
print("Encoded Message:", encoded_message)

# Decode the message
decoded_message = decode(encoded_message, key)
print("Decoded Message:", decoded_message)

# Print the key used for encoding/decoding
print("Key used:", key)
