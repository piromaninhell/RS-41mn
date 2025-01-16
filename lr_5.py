def encode(text):
    # Step 1: Convert each character to its ASCII value and then to 8-bit binary
    binary_message = ''.join(format(ord(c), '08b') for c in text)
    # Step 2: Triple every bit
    tripled_message = ''.join(b * 3 for b in binary_message)
    return tripled_message
def decode(encoded_message):
    # Step 1: Split the encoded message into triplets
    triplets = [encoded_message[i:i+3] for i in range(0, len(encoded_message), 3)]
    # Step 2: Correct each triplet by majority voting
    corrected_bits = []
    for triplet in triplets:
    # Majority voting: If there are more 1s than 0s, the corrected bit is 1, else 0
        corrected_bits.append('1' if triplet.count('1') > triplet.count('0') else '0')
    # Step 3: Group the corrected bits into 8-bit binary sequences
        corrected_message = ''.join(corrected_bits)
    # Step 4: Convert each 8-bit group back to an ASCII value
        chars = []
    for i in range(0, len(corrected_message), 8):
        byte = corrected_message[i:i+8]
        chars.append(chr(int(byte, 2))) # Convert the 8-bit binary to a character
    # Step 5: Join the characters to form the final decoded string
    return ''.join(chars)
# Example usage
encoded = encode("hey")
print("Encoded:", encoded)
decoded = decode(encoded)
print("Decoded:", decoded)
