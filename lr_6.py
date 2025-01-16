def decode_qr(qrcode):
    size = len(qrcode) # QR code size, should be 21 for version 1
    bits = [] # List to store the bit sequence we will extract
    # Step 2: Iterate over the QR code in a zigzag pattern
    for y in range(size-1, -1, -1): # Start from the bottom row
    # Determine if we are moving left or right
        if (size - y) % 2 == 0: # Moving left
            x_range = range(size-1, -1, -1)
        else: # Moving right
            x_range = range(size)
        for x in x_range:
        # Skip the positioning patterns (3 large squares)
            if (x < 7 and y < 7) or (x > size-8 and y < 7) or (x < 7 and y > size-8):
                continue
            # Check mask condition: ((x + y) % 2 == 0)
            mask_condition = (x + y) % 2 == 0
            # Get the bit from the QR code (1 is black, 0 is white)
            bit = qrcode[y][x]
            # Apply mask: flip the bit if the mask condition is true
            if mask_condition:
                bit = 1 - bit # Flip the bit (0 -> 1, 1 -> 0)
                # Add the bit to the sequence
            bits.append(bit)
    # Step 3: Process the bits to extract the message
    # First 4 bits: Mode (we can ignore this as it is always byte mode "0100")
    mode = bits[:4]
    bits = bits[4:]
    # Next 8 bits: Message length (number of characters)
    message_length = int(''.join(map(str, bits[:8])), 2)
    bits = bits[8:]
    # Now extract the message bits (each character is 8 bits)
    message_bits = bits[:message_length * 8]
    # Convert the message bits into characters
    
    message = []
    for i in range(0, len(message_bits), 8):
        char_bits = message_bits[i:i+8]
        char_code = int(''.join(map(str, char_bits)), 2)
        message.append(chr(char_code))
        
        # Return the decoded message as a string
    return ''.join(message)
    # Test the function with the example QR code
qrcode = [
   [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
[0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
[0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
[1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
[1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1],
[1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
[1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1]
]
# Call the function and print the result
decoded_message = decode_qr(qrcode)
print(decoded_message)  # Expected Output: "Hello"
