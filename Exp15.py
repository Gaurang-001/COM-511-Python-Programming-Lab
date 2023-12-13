# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

# Function to convert text to Morse code
def text_to_morse_code(text):
    morse_code = ''
    for char in text:
        char = char.upper()
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char + ' '  # Preserve unknown characters as is
    return morse_code.strip()

# Function to convert Morse code to text
def morse_code_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for symbol in morse_code:
        if symbol in morse_code_dict.values():
            text += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(symbol)]
        elif symbol == '/':
            text += ' '  # Space between words
        else:
            text += symbol  # Preserve unknown Morse code symbols as is
    return text

# Example usage
text = input("Enter text: ")
morse_code = text_to_morse_code(text)
print("Morse Code:", morse_code)

morse_code_input = input("Enter Morse code: ")
decoded_text = morse_code_to_text(morse_code_input)
print("Decoded Text:", decoded_text)