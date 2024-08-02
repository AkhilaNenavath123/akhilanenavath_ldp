from functions import *
from constants import seed

def main():
    # Example usage
     # Dynamic key (can be any number)
    key = generate_permutation_key(seed)
    permutation_table = create_permutation_table(key)

    message = "Hello, World! 123"
    encoded_message = encode_message(message, permutation_table)
    decoded_message = decode_message(encoded_message, permutation_table)

    print(f"Original message: {message}")
    print(f"Permutation key: {key}")
    print(f"Encoded message: {encoded_message}")
    print(f"Decoded message: {decoded_message}")


if __name__ == "__main__":
    main()