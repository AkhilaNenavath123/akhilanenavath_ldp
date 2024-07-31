import random
import string


# Define the character set
CHAR_SET = string.ascii_letters + string.digits + string.punctuation


def generate_permutation_key(seed):
    random.seed(seed)
    char_list = list(CHAR_SET)
    random.shuffle(char_list)
    return ''.join(char_list)


def create_permutation_table(key):
    permutation_table = {CHAR_SET[i]: key[i] for i in range(len(CHAR_SET))}
    return permutation_table


def encode_message(message, permutation_table):
    encoded_message = ''.join(permutation_table[char] if char in permutation_table else char for char in message)
    return encoded_message


def decode_message(encoded_message, permutation_table):
    reverse_table = {v: k for k, v in permutation_table.items()}
    decoded_message = ''.join(reverse_table[char] if char in reverse_table else char for char in encoded_message)
    return decoded_message


# Example usage
seed = 12345  # Dynamic key (can be any number)
key = generate_permutation_key(seed)
permutation_table = create_permutation_table(key)


message = "Hello, World! 123"
encoded_message = encode_message(message, permutation_table)
decoded_message = decode_message(encoded_message, permutation_table)


print(f"Original message: {message}")
print(f"Permutation key: {key}")
print(f"Encoded message: {encoded_message}")
print(f"Decoded message: {decoded_message}")
