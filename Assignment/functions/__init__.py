import random
from constants import CHAR_SET


def generate_permutation_key(seed):
    random.seed(seed)
    char_list = list(CHAR_SET)
    random.shuffle(char_list)
    return "".join(char_list)


def create_permutation_table(key):
    permutation_table = {CHAR_SET[i]: key[i] for i in range(len(CHAR_SET))}
    return permutation_table


def encode_message(message, permutation_table):
    encoded_message = "".join(
        permutation_table[char] if char in permutation_table else char
        for char in message
    )
    return encoded_message


def decode_message(encoded_message, permutation_table):
    reverse_table = {v: k for k, v in permutation_table.items()}
    decoded_message = "".join(
        reverse_table[char] if char in reverse_table else char
        for char in encoded_message
    )
    return decoded_message