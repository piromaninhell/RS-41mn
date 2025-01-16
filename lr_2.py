from collections import Counter
ENGLISH_COMMON_LETTER = 'E'

def find_shift(encoded_text):
    # Filter only alphabetic characters, and make them uppercase to standardize
    filtered_text = [char.upper() for char in encoded_text if char.isalpha()]
    # Count the frequency of each letter in the filtered text
    frequency = Counter(filtered_text)
    # Find the most common letter in the encoded message
    most_common_letter, _ = frequency.most_common(1)[0]
    # Calculate the shift needed to align the most common letter with 'E'
    shift = (ord(most_common_letter) - ord(ENGLISH_COMMON_LETTER)) % 26
    return shift

def caesar_decrypt(text, shift):
    decrypted_text = []
    
    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Apply reverse Caesar shift to decode
            new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text.append(new_char)
        else:
            # Append non-alphabetic characters without changes
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

# Main decoding function that manages input and output
def decode_message(encoded_text):
    shift = find_shift(encoded_text)
    return caesar_decrypt(encoded_text, shift)

# Input handling and output
encoded_text = input().strip()  # Removes unnecessary leading and trailing spaces from the input
decoded_text = decode_message(encoded_text)
print(decoded_text)  # Outputs exactly the decoded message without additional spaces
