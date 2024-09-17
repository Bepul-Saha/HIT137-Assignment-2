# Caesar Cipher decryption function
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_message = ''
    
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            shift_value = ord('A') if char.isupper() else ord('a')
            # Perform the shift and wrap around the alphabet
            decrypted_char = chr((ord(char) - shift_value - shift) % 26 + shift_value)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char  # Non-alphabetic characters remain unchanged
    
    return decrypted_message

# Test all possible shift values to find the original quote
def find_correct_shift(ciphertext):
    for shift in range(1, 26):  # Try all shift values from 1 to 25
        decrypted_message = decrypt_caesar_cipher(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_message}")

# Example ciphered quote
ciphered_quote = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Find the correct shift value
find_correct_shift(ciphered_quote)
