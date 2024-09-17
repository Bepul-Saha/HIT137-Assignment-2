# Step 1: Separate the string into numbers and letters
def separate_string(s):
    number_string = ''
    letter_string = ''
    
    for char in s:
        if char.isdigit():
            number_string += char
        elif char.isalpha():
            letter_string += char
    
    return number_string, letter_string

# Step 2: Convert even numbers in the number string to ASCII decimal values
def convert_even_numbers_to_ascii(number_string):
    ascii_values = []
    
    for char in number_string:
        if int(char) % 2 == 0:  # Check if the number is even
            ascii_values.append(ord(char))
    
    return ascii_values

# Step 3: Convert uppercase letters in the letter string to ASCII decimal values
def convert_uppercase_letters_to_ascii(letter_string):
    ascii_values = []
    
    for char in letter_string:
        if char.isupper():  # Check if the letter is uppercase
            ascii_values.append(ord(char))
    
    return ascii_values

# Example usage
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'

# Separate the string into numbers and letters
number_string, letter_string = separate_string(s)

# Convert even numbers and uppercase letters to ASCII code decimal values
even_numbers_ascii = convert_even_numbers_to_ascii(number_string)
uppercase_letters_ascii = convert_uppercase_letters_to_ascii(letter_string)

print(f"Number string: {number_string}")
print(f"Letter string: {letter_string}")
print(f"Even numbers in ASCII: {even_numbers_ascii}")
print(f"Uppercase letters in ASCII: {uppercase_letters_ascii}")
