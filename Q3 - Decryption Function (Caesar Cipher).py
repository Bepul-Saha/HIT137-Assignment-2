def decrypt(text, key):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Example of how to decrypt:
encrypted_code = "tybony_inevnoyr = 100 zl_qvpg = {'xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'}\nqrs cebprff_ahzoref():"
key = 13  # Example Caesar cipher shift key
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)
