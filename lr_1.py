def caesar_shift(text, shift):
    # Incremental Caesar shift
    result = []
    for i, char in enumerate(text):
        new_char = chr((ord(char) - ord('A') + shift + i) % 26 + ord('A'))
        result.append(new_char)
    return ''.join(result)

def rotor_substitution(text, rotor):
    # Substitutes each character in text with its rotor mapping
    result = []
    for char in text:
        result.append(rotor[ord(char) - ord('A')])
    return ''.join(result)

def rotor_reverse_substitution(text, rotor):
    # Reverse mapping for decoding
    reverse_rotor = ''.join(chr(rotor.index(chr(i + ord('A'))) + ord('A')) for i
    in range(26))
    result = []
    for char in text:
        result.append(reverse_rotor[ord(char) - ord('A')])
    return ''.join(result)

def enigma_machine(action, n, rotor1, rotor2, rotor3, message):
    if action == "ENCODE":
        # Step 1: Caesar shift with incrementing number
        shifted_message = caesar_shift(message, n)

        # Step 2: Pass through the rotors
        encoded_message = rotor_substitution(shifted_message, rotor1)
        encoded_message = rotor_substitution(encoded_message, rotor2)
        encoded_message = rotor_substitution(encoded_message, rotor3)
        return encoded_message
    elif action == "DECODE":
        # Reverse through the rotors for decoding
        decoded_message = rotor_reverse_substitution(message, rotor3)
        decoded_message = rotor_reverse_substitution(decoded_message,rotor2)
        decoded_message = rotor_reverse_substitution(decoded_message,rotor1)
        # Reverse Caesar shift
        reversed_caesar_message = []
        for i, char in enumerate(decoded_message):
            shift_value = n + i
            new_char = chr((ord(char) - ord('A') - shift_value + 26) % 26 + ord('A'))
            reversed_caesar_message.append(new_char)
        return ''.join(reversed_caesar_message)

# Reading input
action = input().strip() # Either "ENCODE" or "DECODE"
n = int(input().strip()) # Starting shift N
rotor1 = input().strip() # First rotor substitution sequence
rotor2 = input().strip() # Second rotor substitution sequence
rotor3 = input().strip() # Third rotor substitution sequence
message = input().strip() # Message to encode or decode

# Running the Enigma machine
result = enigma_machine(action, n, rotor1, rotor2, rotor3, message)
print(result) # Output the result
