import random
import string

# Function to generate a key
def generate_key():
    characters = string.ascii_letters + string.digits + string.punctuation
    key = list(characters)
    random.shuffle(key)
    return ''.join(key)

# Function to encode a message using the key
def encode(message, key):
    characters = string.ascii_letters + string.digits + string.punctuation
    char_to_key = {char: key[i] for i, char in enumerate(characters)}
    encoded_message = ''.join(char_to_key.get(char, char) for char in message)
    return encoded_message

# Function to decode an encoded message using the key
def decode(encoded_message, key):
    characters = string.ascii_letters + string.digits + string.punctuation
    key_to_char = {key[i]: char for i, char in enumerate(characters)}
    decoded_message = ''.join(key_to_char.get(char, char) for char in encoded_message)
    return decoded_message

# Generate a key
key = generate_key()

# Original message
message = input("Enter the message: ")

# Encode the message
encoded_message = encode(message, key)
print("Encoded Message:", encoded_message)

# Decode the message
decoded_message = decode(encoded_message, key)
print("Decoded Message:", decoded_message)

# Print the key used for encoding/decoding
print("Key used:", key)
